from statistics import mode
from django.db import models

# Create your models here.
class test_table(models.Model):
    name = models.CharField(max_length=50)
    introduction = models.TextField()
    area = models.CharField(max_length=50)
    party_number = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class parameter(models.Model):
    icc1 = models.FloatField(max_length=10)
    icc2 = models.FloatField(max_length=10)
    name = models.CharField(max_length=10)
    sample = models.CharField(max_length=10)
    Field5 = models.FloatField(max_length=10)
    
    def __str__(self):
        return self.name

class ctrl(models.Model):
    name = models.CharField(max_length=10)
    ud = models.FloatField(max_length=10)
    nd = models.FloatField(max_length=10)
    phyh = models.FloatField(max_length=10)
    phyl = models.FloatField(max_length=10)

    def __str__(self):
        return self.name