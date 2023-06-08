from django.db import models

class Property(models.Model):
    name= models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    # price = models.Integ
    # status = models.
    # bedrooms = models.
    # bathrooms = models.
    # description = models.
    # location = models.
    # sqft = models.
    # date_listed = models.