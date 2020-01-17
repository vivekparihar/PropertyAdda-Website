from django.db import models

# Create your models here.

class forSale(models.Model):
    propertyName = models.CharField(max_length=50)
    propertyType = models.CharField(max_length=50)
    propertyDesc = models.CharField(max_length=1000)
    propertyCity = models.CharField(max_length=50)
    propertyPrice = models.IntegerField(default=0)
    propertyOwner = models.CharField(max_length=50)
    ownerContact = models.CharField(max_length=10, default=0)
    image = models.ImageField(upload_to="for-sale")

class forRent(models.Model):
    propertyName = models.CharField(max_length=50)
    propertyType = models.CharField(max_length=50)
    propertyDesc = models.CharField(max_length=1000)
    propertyCity = models.CharField(max_length=50)
    propertyRent = models.IntegerField(default=0)
    propertyOwner = models.CharField(max_length=50)
    ownerContact = models.CharField(max_length=10, default=0)
    image = models.ImageField(upload_to="for-sale")

class sellers(models.Model):
    propertyName = models.CharField(max_length=50)
    propertyType = models.CharField(max_length=50)
    propertyDesc = models.CharField(max_length=1000)
    propertyCity = models.CharField(max_length=50)
    propertyOwner = models.CharField(max_length=50)
    businessType = models.CharField(max_length=50)
    propertyPrice = models.CharField(max_length=50)
    ownerContact = models.CharField(max_length=10, default=0)
    image = models.ImageField(upload_to="to-sell")


