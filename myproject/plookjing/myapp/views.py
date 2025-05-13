from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Tree, UserPlanting
from django.db.models import Q, Count
from .forms import UserPlantingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics
from .serializers import TreeSerializer

# หน้าแรก (Function-Based View)
def home(request):
    return render(request, 'myapp/home.html')

# รายการต้นไม้ (Class-Based View)
class TreeListView(ListView):
    model = Tree
    template_name = 'myapp/tree_list.html'
    context_object_name = 'trees'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-price')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(species__icontains=query)
            )
        return queryset

# รายละเอียดต้นไม้
class TreeDetailView(DetailView):
    model = Tree
    template_name = 'myapp/tree_detail.html'
    context_object_name = 'tree'

# ปลูกต้นไม้
class PlantTreeView(LoginRequiredMixin, CreateView):
    model = UserPlanting
    form_class = UserPlantingForm
    template_name = 'myapp/plant_tree.html'
    success_url = reverse_lazy('tree_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.tree = Tree.objects.get(pk=self.kwargs['pk'])
        # location อาจถูกตั้งค่าในขั้นตอนอื่น หรือสามารถกำหนดจากค่าคงที่/ค่า default
        form.instance.location = form.instance.location  # สมมติว่า location ถูกกำหนดภายนอก
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tree'] = Tree.objects.get(pk=self.kwargs['pk'])
        return context

# API - List and Create Tree
class TreeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

# API - Retrieve and Update Tree
class TreeRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

# Dashboard สำหรับผู้ดูแล
def dashboard(request):
    total_trees = Tree.objects.count()
    total_users = UserPlanting.objects.values('user').distinct().count()
    total_plantings = UserPlanting.objects.count()
    recent_plantings = UserPlanting.objects.select_related('tree', 'location').order_by('-planting_date')[:5]

    context = {
        'total_trees': total_trees,
        'total_users': total_users,
        'total_plantings': total_plantings,
        'recent_plantings': recent_plantings,
    }
    return render(request, 'myapp/dashboard.html', context)
