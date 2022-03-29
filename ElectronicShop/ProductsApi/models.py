from django.db import models


class ElectronicProducts(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Type_list = (('MO', 'Mobile'), ('LAP', 'Laptop'))
    Type = models.CharField(choices=Type_list, default='NAN', max_length=200)
    Processor = models.CharField(max_length=200,default='NAN')
    RAM = models.IntegerField(default=0)
    Screensize = models.FloatField(default=0)
    HDCapacity = models.IntegerField(default=0)
    Color = models.CharField(max_length=200, default='NAN')
