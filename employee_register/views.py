from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_list(request):
    employee_list = Employee.objects.all() 
    return render(request, 'employee_register/employee_list.html', {'employee_list' : employee_list})

def employee_form(request, id=0):
    if request.method == 'GET':
           # form = EmployeeForm()
           # return render(request, 'employee_register/employee_form.html', {'form' : form})
        if id==0:
            form = EmployeeForm()
            return render(request, 'employee_register/employee_form.html', {'form' : form})
        else:
            employee = Employee.objects.get(pk= id)
            form = EmployeeForm(instance=employee) 
            return render(request, 'employee_register/employee_form.html', {'form' : form})   
            #return render(request, 'employee_register/employee_form.html', {'employee_id' : employee_id})
        
        
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk= id)
            form = EmployeeForm(request.POST, instance = employee)
        
        if form.is_valid():
            form.save()
        return redirect('employee_list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk= id)
    employee.delete()
    return redirect('employee_list')