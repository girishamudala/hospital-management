from django.db import models

# Create your models here.

class OP(models.Model):
    o_id= models.IntegerField(primary_key=True)
    p_id= models.IntegerField()
    o_date= models.DateTimeField()
    o_pname= models.CharField(max_length=50)
    symptoms= models.CharField(max_length=50)
    doctor_assign= models.CharField(max_length=50)

    def __str__(self):
        return str(self.o_id)+" " + (self.o_pname)


class Patient(models.Model):
    gender_choices=[
        ('m','male'),
        ('f','female'),
        ('o','others')
    ]
    p_id= models.IntegerField(primary_key=True)
    p_name= models.CharField(max_length=50)
    p_weight= models.IntegerField()
    p_BP= models.IntegerField()
    p_gender= models.CharField(max_length=1, choices=gender_choices)
    p_phone= models.IntegerField()
    p_aadhar= models.IntegerField()
    p_address= models.TextField(max_length=100)
    admitted_date= models.DateTimeField()
    discharge_date= models.DateTimeField()
    op = models.ForeignKey(OP,on_delete=models.CASCADE)


    class Meta:
        db_table= "patient_details"

    def __str__(self):
        return str(self.p_id) + " " + (self.p_name)
         
