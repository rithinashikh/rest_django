from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework.response import Response

def index(request):
    return render(request,'index.html')

class EmployeeList(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)
