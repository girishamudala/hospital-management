from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models.models_s import Op,Patient
from rest_framework import generics
from core.serializers import Opserializer,Patientserializer

class Patientcreate(APIView):
    def get(self, request):
        try:
            patobj = Patient.objects.all()
            patserializerobj = Patientserializer(patobj, many = True)
        except:
            return Response("given patient object url not found", status=status.HTTP_205_RESET_CONTENT)

        return Response(patserializerobj.data, status=status.HTTP_200_OK)


    def post(self,request):
        patserializer = Patientserializer(data=request.data)
        if patserializer.is_valid():
            patserializer.save()
            return Response(patserializer.data, status=status.HTTP_201_CREATED)
        return Response("enter valid patient details", status=status.HTTP_400_BAD_REQUEST)

class Single_patientdetailsview(APIView):
    def get(self,request,pk):
        try:
            patobj = Patient.objects.get(pk=pk)
            patserializerobj = Patientserializer(patobj)
        except:
            return Response("please enter valid patient id",status=status.HTTP_400_BAD_REQUEST)
        return Response(patserializerobj.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        patobj = Patient.objects.get(pk=pk)
        """if we didnt given pk =pk it shows cannot unpack non-iterable int object"""
        patserializerobj = Patientserializer(patobj, data = request.data)
        if patserializerobj.is_valid():
            patserializerobj.save()
            return Response(patserializerobj.data , status=status.HTTP_201_CREATED)        
        return Response('enter valid patient attributes', status=status.HTTP_205_RESET_CONTENT)
    
    def delete(self,request,pk):
        patobj = Patient.objects.get(pk=pk)
        patobj.delete()
        return Response('removed data from database successfully', status=status.HTTP_204_NO_CONTENT)



# class Patientview(generics.GenericAPIView):
#     def get_queryset(self):
#         return Patient.objects.all()
#     def get(self,request,*args, **kwargs):
#         pat_qs = self.get_queryset()
#         pat_dct = []
#         for pat in pat_qs: 
#             dpat = {}
#             dpat['p_id']= pat.p_id
#             dpat['p_name'] = pat.p_name 
#             dpat['p_age'] = pat.p_age 
#             dpat['p_gender']= pat.p_gender 
#             dpat['p_phone']= pat.p_phone 
#             dpat['p_aadhar']= pat.p_aadhar 
#             dpat['p_address']= pat.p_address 
#             dpat['admitted_date']= pat.admitted_date 
#             dpat['discharge_date']= pat.discharge_date 
#             dpat['visits'] = pat.visits 
#             dpat['op'] = pat.op
#             pat_dct.append(dpat)
#         return Response(pat_dct, status=status.HTTP_200_OK)


            





# class Opdetails(generics.ListCreateAPIView):
#     queryset = Op.objects.all()
#     serializer_class = Opserializer

# class Patientview(generics.ListCreateAPIView):
#     queryset = Patient.objects.prefetch_related('op').all()
#     serializer_class = Patientserializer


