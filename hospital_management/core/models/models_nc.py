from django.db import models


class Department(models.Model):
    #id=models.IntegerField(null=True)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Doctor(models.Model):
    id=models.IntegerField(null=True)
    name=models.CharField(max_length=100)
    experiance=models.IntegerField(null=True)
    specialization=models.CharField(max_length=100)
    
    def __str__(self):
        return self.specialization