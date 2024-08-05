# models.py
from django.db import models
from django.utils import timezone

class HomeProduct(models.Model):
    image = models.ImageField(upload_to="project_images/home_products/")

    def __str__(self):
        return str(self.image)

class SparePart(models.Model):
    image = models.ImageField(upload_to="project_images/spare_parts/")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    details = models.JSONField(default=dict)  # Updated to JSONField
    category = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.FloatField(blank=True, null=True)
    old_price = models.FloatField(blank=True, null=True)
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Truck(models.Model):
    image = models.ImageField(upload_to="project_images/trucks/")
    category = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    details = models.JSONField(default=dict)  # Assuming you want this for Truck too
    new = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Equipment(models.Model):
    image = models.ImageField(upload_to="project_images/equipment/")
    category = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    details = models.JSONField(default=dict)  # Updated to JSONField
    new = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to="project_images/blogs/", blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
