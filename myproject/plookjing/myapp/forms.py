from django import forms
from .models import UserPlanting

class UserPlantingForm(forms.ModelForm):
    class Meta:
        model = UserPlanting
        fields = []  # ไม่ต้องกรอกเองในฟอร์ม (กำหนด user, tree, location และ planting_date ผ่านโค้ด)
