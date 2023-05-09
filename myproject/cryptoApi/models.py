from django.db import models

class Address(models.Model):
    coin = models.CharField(max_length=3)
    address = models.CharField(max_length=50)