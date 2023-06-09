from django.db import models
from django.utils import timezone
import datetime

class Property(models.Model):
    name= models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200, default='')
    price = models.IntegerField(default=1)
    status = models.CharField(max_length=50, default='')
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.DecimalField(max_digits=4, decimal_places=2, default=1)
    description = models.TextField(default='')
    location = models.CharField(max_length=100, default=1)
    sqft = models.IntegerField(default=1)
    date_listed = models.DateField(default=datetime.date.today)
    image = models.ImageField(upload_to='property_images')

    def __str__(self):
        return self.name
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    subject = models.CharField(max_length=200, default='')
    message = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject