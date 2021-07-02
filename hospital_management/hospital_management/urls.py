"""hospital_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views.views_s import Patientcreate , Single_patientdetailsview
# from core.views.views_s import Patientview, Patientcreate
# Patientview
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('patdetails/', Patientview.as_view()),
    # path('opdetails/', Opdetails.as_view()),
    path('patdetails/', Patientcreate.as_view()),
    path('singlepatdetails/<int:pk>/', Single_patientdetailsview.as_view()),
]
