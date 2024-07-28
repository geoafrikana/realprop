from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=700)
    address = models.CharField(max_length=255)
    LGA = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(default='nga', max_length=150)
    price = models.IntegerField()
    property_type = models.CharField(max_length=155)
    latitude = models.DecimalField(max_digits=6, decimal_places=3)
    longitude = models.DecimalField(max_digits=6, decimal_places=3)
    picture = models.ImageField(upload_to='property_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name
