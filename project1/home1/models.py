from django.db import models

# Create your models here.

class Product(models.Model):
    id= models.IntegerField(auto_created=True, primary_key=True)
    name= models.TextField(default='abc')
    status= models.TextField(default='hello')
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

