from django.shortcuts import render
from django.http import HttpResponse
from .Forms import UserForm

def index(request):
    return HttpResponse("Hello World")

def create(request):
    if request.method == 'GET':
        form = UserForm()

        context = {

            'form':form,

        }
    
    return render(request,'user/criar.html',context=context)