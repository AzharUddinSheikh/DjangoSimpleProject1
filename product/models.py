from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stocks = models.IntegerField()
    image = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    discount = models.FloatField()
