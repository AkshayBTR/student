from django.shortcuts import render
from myapp import forms
from myapp.models import *
# Create your views here.
def create_student(request):
    if request.method=="POST":
        form=forms.Std_Form(request.POST)
        form.save()
    form=forms.Std_Form()
    return render(request,"create_student.html",context={'form':form})

def search(request):
    return render(request,'search_student.html')

def display(request):
    if request.method=="POST":
        Phno = request.POST["Phno"]
        Email = request.POST["Email"]
        Percentage = request.POST["Percentage"]
        YOP = request.POST["YOP"]
        qs=Student_Details.objects.None()
        if Phno!="None":
            qs=qs|Student_Details.objects.filter(Phno=Phno)
        if Email!="None":
            qs=qs|Student_Details.objects.filter(Email=Email)
        if Percentage!="None":
            qs=qs|Student_Details.objects.filter(Percentage=Percentage)
        if YOP!="None":
            qs=qs|Student_Details.objects.filter(YOP=YOP)
        if Phno=="None" and Email=="None" and Percentage=="None" and YOP=="None":
            qs=Student_Details.objects.all()
    return render(request,"dipsaly.html",context={"students":qs})

        