from django.db import models

class Property(models.Model):
    name= models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    price = models.IntegerField()
    status = models.CharField(max_length=50)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    location = models.CharField(max_length=100)
    sqft = models.IntegerField()
    date_listed = models.DateField(auto_now_add=True)