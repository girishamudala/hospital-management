from django.contrib import admin
from core.models.models_s import Patient,Op
from core.models.models_rd import Visit
from core.models.models_nc import Doctor, Department
from core.models.models_rm import Test, Medicine

# Register your models here.hospital


admin.site.register(Patient)
admin.site.register(Op)
admin.site.register(Visit)
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Test)
admin.site.register(Medicine)