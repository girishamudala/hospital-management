from django.db import models
from core.models.models_nc import Doctor

# Create your models here.

class Op(models.Model):
    o_id= models.IntegerField(primary_key=True)
    o_date= models.DateTimeField()
    o_pname= models.CharField(max_length=50)
    symptoms= models.CharField(max_length=50)
    doctor_assign= models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.o_pname +" "+str(self.o_id)


class Patient(models.Model):
    gender_choices=[
        ('m','male'),
        ('f','female'),
        ('o','others')
    ]
    p_id= models.IntegerField(primary_key=True)
    p_name= models.CharField(max_length=50)
    p_age = models.IntegerField()
    p_gender= models.CharField(max_length=1, choices=gender_choices)
    p_phone= models.IntegerField()
    p_aadhar= models.IntegerField()
    p_address= models.TextField(max_length=100)
    admitted_date= models.DateTimeField()
    discharge_date= models.DateTimeField()
    visits = models.IntegerField(null=True)
    op = models.ForeignKey(Op, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.p_id) + " " + (self.p_name)
         
