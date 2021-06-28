from django.db import models

# Create your models here.

class Product(models.Model):
    name= models.CharField(max_length=25, null= False, blank=False)
    category=  models.CharField(max_length=25, null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    description = models.TextField()
    start= models.IntegerField()

    def __str__(self):
        return self.name
