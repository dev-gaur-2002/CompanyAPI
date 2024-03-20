from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls import include
from api.views import CompanyViewset, EmployeeViewset

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewset)
router.register(r'employees', EmployeeViewset)

urlpatterns = [
    path('', include(router.urls)),
]
