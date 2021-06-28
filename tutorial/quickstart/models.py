from django.db import models

# Create your models here.

class sp(models.Model):
    id= models.IntegerField()
    id = models.AutoField(primary_key=True)
    name= models.TextField()
    logo= models.TextField()

    def __str__(self):
        return self.name
    