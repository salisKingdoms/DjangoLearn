from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Employees
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt


# Create your views here.
def index(request):
    return render(request, 'employees/index.html')

def employee_list(request):
    employees = list(Employees.objects.values())
    return JsonResponse({'data':employees})

def employee_create(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        #data = json.loads(request.body)
        emp = Employees.objects.create(
            name = data['name'],
            email =data['email'],
            department =data['department'],
            salary =data['salary']
        )
        return JsonResponse({'id':emp.id, 'message':'employee created success'})
# Kalau GET (atau method lain), balikin response error yang jelas
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def employee_update(request, id):
    emp = get_object_or_404(Employees, pk=id)
    if request.method == 'POST':
        data = json.loads(request.body)
        emp.name = data['name']
        emp.email = data['email']
        emp.department = data['department']
        emp.salary = data['salary']
        emp.save()
        return JsonResponse({'message':'employee update success'})


def employee_delete(request, id):
    emp = get_object_or_404(Employees, pk=id)
    emp.delete()
    return JsonResponse({'message':'employee delete success'})