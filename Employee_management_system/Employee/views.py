from django.shortcuts import render,redirect
from Employee.models import Employee
# Create your views here.
def add(request):
    if (request.method=="POST"):
        name_ = request.POST["name"]
        age_ = request.POST["age"]
        salary_ = request.POST["salary"]
        city_ = request.POST["city"]
        print(name_)
        print(age_)
        print(salary_)
        print(city_)

        insert_data = Employee.objects.create(name=name_, age=age_, salary=salary_, city=city_)

        insert_data.save()
        return redirect("/")
    return render(request,'employee/emp.html')


def index(request):
    content ={}
    #content['data'] =Employee.objects.all()
    content['data'] =Employee.objects.filter(is_deleted="n")
    return render(request,'employee/index.html',content)

def delete(request,tid):
    record_to_be_deleted = Employee.objects.filter(id=tid)
    record_to_be_deleted.update(is_deleted="y")
    return redirect("/")

def update(request,tid):
    if (request.method=="POST"):
        name_ = request.POST["name"]
        age_ = request.POST["age"]
        salary_ = request.POST["salary"]
        city_ = request.POST["city"]
        record_to_be_update = Employee.objects.filter(id=tid)
        record_to_be_update.update(name=name_, age=age_, salary=salary_, city=city_)
        return redirect("/")
    else:
        content ={}
        content['data'] =Employee.objects.get(id=tid)
        return render(request,'employee/update.html',content)
