from django.shortcuts import redirect, render, get_object_or_404  , HttpResponse
from django.urls import reverse  
from django.views.decorators.clickjacking import xframe_options_exempt,xframe_options_deny
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import *

from  django.contrib.auth.models import User
from  accounts.models import Visitor
from  accounts.urls import register
from .models import *
from .forms import *
from .templates import *
from .static import *


#############HOME###############
@login_required(login_url='login')
def Home_visitors(request):
    context = {'message':'WELCOME TO LIBRARY SITE!!'}
    if request.method=='GET':
        try:
            user = request.user
            context = {'message':f'HI {user} !! WELCOME TO LIBRARY SITE !!'}
        except:
            context = {'message':'WELCOME TO LIBRARY SITE!!'}
    return render(request,'Home_visitors.html',context)

@xframe_options_exempt
def carusel_visitors(request):
    return  render(request,'carusel_visitors.html',{})

@xframe_options_deny
def view_one(request):
    return HttpResponse("<h1>Can't display in this version!</h1>")


###############books#############
def books_search(request,l_books):
    
    if l_books: 
        books = l_books
    else:
        books = Book.objects.all()

   
    if request.GET.get("identication"):     
        books = books.filter(identication = request.GET.get("identication"))
    if request.GET.get("name"):
        books = books.filter(nameֹ__icontains = request.GET.get("name"))
    if request.GET.get("author"):
        books = books.filter(authorֹ__icontains = request.GET.get("author"))
    if request.GET.get("published_year"):
        books = books.filter(published_year = int(request.GET.get("published_year")))
    if request.GET.get("book_type"):
        books = books.filter(book_type = int(request.GET.get("book_type")))

    if len(books)==0:
        request.session['errors'] = 'BOOK NOT FOUND !'
        books = l_books
    else:
        request.session['errors'] = ''

    return books

def books_visitors(request):
    errors = ''
    books = Book.objects.all()
    
    if 'search' in request.GET:
        books = books_search(request,books)
        errors = request.session.get('errors')
        
    context = {'books':books , 'errors':errors}
    return render(request,'books_visitors.html',context)


###############loans##############
def loans_visitors(request):
    loans = Loan.objects.filter(customer = request.user.customer).order_by('-borrow_date')
    context = {'loans': loans}

    return render(request,'loans_visitors.html',context)


########Instructions#########
def instructions_visitors(request):
    return render(request,'instructions_visitors.html',{})
