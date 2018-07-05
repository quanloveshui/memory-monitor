from django.db import models

# Create your models here.

class Muse(models.Model):
    muse = models.CharField(max_length=200)
    ctime = models.CharField(max_length=200)
   
    def __str__(self):
        return self.muse
