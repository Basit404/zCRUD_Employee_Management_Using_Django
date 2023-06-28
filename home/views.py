from django.shortcuts import render, HttpResponse, redirect
from home.models import Employee

# Create your views here.

# function for reading data on homepage
def home(request):
    emp = Employee.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, "home.html", context)


# function for adding data
def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        emp = Employee(name=name, email=email, address=address, phone=phone)
        emp.save()
        return redirect("/home")


# function for editing data
def edit(request):
    emp = Employee.objects.all()
    context = {
            'emp': emp,
        }
    return render(request, "home.html", context)


# function for updating data
def update(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        emp = Employee(id=id, name=name, email=email, address=address, phone=phone)
        emp.save()
        return redirect("/home")


# function for deleting data
def delete(request, id):
    emp = Employee.objects.filter(id=id)
    emp.delete()
    return redirect("/home")