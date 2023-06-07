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
    
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

    def put(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)

        updated_data = request.data
        for employee_data in updated_data:
            employee_id = employee_data.get('id')

            try:
                employee = Employee.objects.get(id=employee_id)
                serializer = EmployeeSerializer(employee, data=employee_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=400)
            except Employee.DoesNotExist:
                return Response(f"Employee with ID {employee_id} does not exist.", status=404)

        return Response(serializer.data)
    
    def patch(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)

        updated_data = request.data
        for employee_data in updated_data:
            employee_id = employee_data.get('id')
            try:
                employee = Employee.objects.get(id=employee_id)
                serializer = EmployeeSerializer(employee, data=employee_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=400)
            except Employee.DoesNotExist:
                return Response(f"Employee with ID {employee_id} does not exist.", status=404)

        return Response(serializer.data)
