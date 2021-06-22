from django.db import models

# Create your models here.
class Test(models.Model):
    id = models.IntegerField()
    test_name = models.CharField(max_length=50)
    test_description = models.CharField(max_length=1000)
    price = models.IntegerField()


class Medicine(models.Model):
    id = models.IntegerField()
    medicine_name = models.CharField(max_length=50)
    medicine_description = models.CharField(max_length=1000)
    price = models.IntegerField()