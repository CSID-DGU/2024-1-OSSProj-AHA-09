from django.db import models

# Create your models here.
class data_prediction(models.Model):
    id=models.AutoField(primary_key=True)
    year=models.IntegerField()
    region=models.TextField()
    crop=models.TextField()
    prediction=models.FloatField()