from django.db import models

# Create your models here.
class Data(models.Model):
    crops=models.TextField()
    year=models.IntegerField()
    region=models.TextField()
    prediction=models.FloatField()
