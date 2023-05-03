from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def django_forms(request):
    formobject=StudentForm()
    d={'form':formobject}

    if request.method=="POST":
        FD=StudentForm(request.POST)
        if FD.is_valid():
            n=FD.cleaned_data['name']
            a=FD.cleaned_data['age']
            e=FD.cleaned_data['email']
            g=FD.cleaned_data['gender']
            c=FD.cleaned_data['course']
            return HttpResponse('data is submitted')

    return render(request,'django_forms.html',d)
