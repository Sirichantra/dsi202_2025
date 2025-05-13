from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tree(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class PlantingLocation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserPlanting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    location = models.ForeignKey(PlantingLocation, on_delete=models.CASCADE)
    planting_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.tree.name} at {self.location.name}"
