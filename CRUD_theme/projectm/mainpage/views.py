from django.shortcuts import render
from mainpage.models import Student
# Create your views here.
def indexpage(request):
    z=Student.objects.all()
    if request.method=="POST":
        a=request.POST['name']
        b=request.POST['email']
        c=request.POST['password']
        x=Student(Name=a,Email=b,Password=c)
        x.save()
    return render(request,"index.html",{'z':z})

def delete(request,myid):
    x=Student.objects.get(id=myid)
    x.delete()
    return redirect('/')

def edit(request,myid):
     if request.method=="POST":
        m=request.POST['Name']
        n=request.POST['Email']
        o=request.POST['Password']
        p=Student.objects.get(id=myid)
        p.Name=m
        p.Email=n
        p.Password=o
        p.save()
        z=Student.objects.all()
        return redirect('indexpage')
     return render(request,"edit.html")
        
    
    

    
