from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action


# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employee(self,request,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(comapany = company)
            emp_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': "invalid company id"
            })

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer