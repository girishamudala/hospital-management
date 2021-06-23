from django.db import models
from models.models_s import OP, Patient
from models.models_rm import Test, Medicine
from models.models_nc import Department, Doctor

class Visit(models.Model):
    #visit_id=models.IntegerField()
    op_id=models.ForeignKey(OP, on_delete=models.CASCADE)
    patient_id=models.ForeignKey(Patient, on_delete=models.CASCADE)
    department_id=models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor_id=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    test_id=models.ForeignKey(Test, on_delete=models.CASCADE)
    medicine_id=models.ForeignKey(Medicine, on_delete=models.CASCADE)
    date_time=models.DateTimeField()
    is_next_visit=models.BooleanField(default=False)

    def __str__(self):
        return self.id
    
