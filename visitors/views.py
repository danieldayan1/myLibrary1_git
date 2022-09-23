from django.shortcuts import redirect, render, get_object_or_404  , HttpResponse
from django.urls import reverse  
from django.views.decorators.clickjacking import xframe_options_exempt,xframe_options_deny
from django.views.generic import ListView
import pickle,os,random , csv , statistics
import re , functools , random , copy 
from abc import abstractmethod , ABCMeta
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm , authenticationForm
# from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *
from .templates import *
from .static import *



def Home(request):
    context = {'message':'WELCOME TO LIBRARY SITE!!'}
    if request.method=='GET':
        myName = request.GET.get('myName')
        password = request.GET.get('password')
        try:
            user = request.user
            context = {'message':f'HI {user.name} !! WELCOME TO LIBRARY SITE !!'}
        except:
            context = {'message':'WELCOME TO LIBRARY SITE!!'}
    return render(request,'Home.html',context)


    return render(request,'contact.html',{})

@xframe_options_exempt
def carusel(request):
    return  render(request,'carusel.html',{})

@xframe_options_deny
def view_one(request):
    return HttpResponse("<h1>Can't display in this version!</h1>")







