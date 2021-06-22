from django.db import models

# Create your models here.
class Test(models.Model):
    test_name = models.CharField(max_length=50)
    test_description = models.CharField(max_length=1000)
    price = models.IntegerField()

    def __str__(self):
        return self.test_name

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=50)
    medicine_description = models.CharField(max_length=1000)
    price = models.IntegerField()

    def __str__(self):
        return self.medicine_name

