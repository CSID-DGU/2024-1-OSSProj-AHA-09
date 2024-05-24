from django.db import models

# Create your models here.
class Rice(models.Model):
    year=models.IntegerField()
    region=models.TextField()
    prediction=models.FloatField()

class Barley(models.Model):
    year=models.IntegerField()
    region=models.TextField()
    prediction=models.FloatField()

class Corn(models.Model):
    year=models.IntegerField()
    region=models.TextField()
    prediction=models.FloatField()

class Bean(models.Model):
    year=models.IntegerField()
    region=models.TextField()
    prediction=models.FloatField()