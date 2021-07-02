from rest_framework import serializers
from core.models.models_s import Op,Patient

class Opserializer(serializers.ModelSerializer):
    class Meta:
        model = Op
        fields= "__all__"

class Patientserializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"