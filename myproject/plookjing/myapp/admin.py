from django.contrib import admin
from .models import Tree, Equipment, PlantingLocation, UserPlanting

@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'image_url')
    list_editable = ('price',)
    search_fields = ('name',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image_url')
    list_editable = ('price',)
    search_fields = ('name',)

@admin.register(PlantingLocation)
class PlantingLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location_type', 'description')
    list_filter = ('location_type',)
    search_fields = ('name', 'location_type')

@admin.register(UserPlanting)
class UserPlantingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'tree', 'location', 'planting_date')
    list_filter = ('planting_date', 'location__name', 'tree__name')
    search_fields = ('user__username', 'tree__name', 'location__name')
