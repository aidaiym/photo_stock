from django.db import models

# Create your models here.
class Photo(models.Model):
    tittle = models.CharField(max_length = 100, blank= False)
    description = models.CharField(max_length=250) 
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title