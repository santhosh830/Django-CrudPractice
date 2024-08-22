from django.shortcuts import render,redirect
from .forms import employeeForm
from.models import Employee
# Create your views here.

def index(request):
    obj = Employee.objects.all()
    context ={
        'data':obj
    }
    return render(request, "index.html", context)



def create(request):
    if request.method == "POST":
        form = employeeForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('read')
        return redirect('create')
    else:
        form = employeeForm   
    context = {
        'form':form
    }
    return render(request, "create.html", context)



def update(request, id):
    obj = Employee.objects.get(id = id)
    if request.method == "POST":
        form = employeeForm(request.POST, instance=obj)
        if form.is_valid():
          form.save()
          return redirect('read')
        return redirect('update')
    else:
        form = employeeForm   
    context = {
        'form':form
    }
    return render(request, "update.html", context)


def delete(request,id):
    obj = Employee.objects.get(id=id)
    obj.delete()
    return redirect('read')


