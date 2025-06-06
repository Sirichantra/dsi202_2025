# Generated by Django 5.1.6 on 2025-05-24 14:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_purchase_equipment_remove_purchase_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('verifying', 'กำลังตรวจสอบ'), ('preparing', 'กำลังจัดเตรียม'), ('shipping', 'กำลังจัดส่ง'), ('delivered', 'จัดส่งสำเร็จ'), ('cancelled', 'ยกเลิกแล้ว')], default='verifying', max_length=50),
        ),
        migrations.CreateModel(
            name='TreePaymentProof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slip', models.ImageField(upload_to='tree_slips/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.plantinglocation')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tree')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TreePaymentSlip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tree_slips/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tree')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
