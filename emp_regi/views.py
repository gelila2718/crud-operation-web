from django.shortcuts import render, redirect
from emp_regi.forms import EmployeeForm
from emp_regi.models import Employee
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show")
    else:
        form = EmployeeForm()
    return render(request, "index.html", {"form": form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {"employees": employees})



def edit(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    return render(request, 'edit.html', {'employee': employee})




def update(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("show")  
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'edit.html', {'form': form, 'employee': employee})


def destroy(request, emp_id):
    try:
        employee = Employee.objects.get(emp_id=emp_id)
        employee.delete()
        return redirect(
            "show"
        ) 
    except Employee.DoesNotExist:
        return HttpResponseNotFound("Employee not found")
