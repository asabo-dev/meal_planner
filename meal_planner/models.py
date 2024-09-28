from django.db import models

# Create your models here.
class Cuisine(models.Model):
    """Type of cuisine"""
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Drink(models.Model):
    """Type of drink"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name