from django.shortcuts import redirect, render, get_object_or_404  , HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt,xframe_options_deny
from datetime import *
from  django.contrib.auth.models import User
from  accounts.models import Visitor
from  visitors.models import Book , Loan
from  accounts.urls import register

from .models import *
from .forms import *
from .templates import *
from .static import *


##########Home#########
def Home_staff(request):
    context = {'message':'WELCOME TO LIBRARY SITE!!'}
    if request.method=='GET':
        try:
            user = request.user
            context = {'message':f'HI {user} !! WELCOME TO LIBRARY SITE !!'}
        except:
            context = {'message':'WELCOME TO LIBRARY SITE!!'}
    return render(request,'Home_staff.html',context)

@xframe_options_exempt
def carusel_staff(request):
    return  render(request,'carusel_staff.html',{})

@xframe_options_deny
def view_one(request):
    return HttpResponse("<h1>Can't display in this version!</h1>")


#########Books#########
def books_search(request,l_books):
    
    if l_books: 
        books = l_books
    else:
        books = Book.objects.all()

   
    if request.GET.get("identication"):     
        books = books.filter(identication = request.GET.get("identication"))
    if request.GET.get("name"):
        books = books.filter(name = request.GET.get("name"))
    if request.GET.get("author"):
        books = books.filter(author = request.GET.get("author"))
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

def books_staff(request):

    errors = ''
    books = Book.objects.all()

    if 'search' in request.GET:
        books = books_search(request,books)
        errors = request.session.get('errors')
    elif 'add' in request.GET:
        return redirect('add_book')
    elif 'del' in request.GET:
        book_id =  int(request.GET.get('book'))
        book = get_object_or_404(Book,identication = book_id)
        free_books = calc_free_books()
        if book in free_books:
            book.delete()
        else:
            errors = "book already in loan !"
 
    context = {'books':books , 'errors':errors}
    return render(request,'books_staff.html',context)

def calc_free_books():

    active_books = []
    free_books = []

    active_loans = Loan.objects.filter(return_date = None)
    active_books = active_loans.values_list('books')
    free_books = Book.objects.exclude(identication__in  = active_books)

    return free_books

def add_book(request):
    
    errors = ""
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            respnose_cont ='<a href = "/staff/books_staff"> BOOK ADDED SUCCEFULY ! CLICK HERE TO RETURN TO BOOKS LIST ...</a>'
            return HttpResponse(respnose_cont)
        else:
            errors = form.errors
        
    content = {'form':form,'errors':errors}
    return render(request,'add_book.html',content)


########Loans###########
def loans_staff(request):
    loans = Loan.objects.all().order_by('-borrow_date')
    context = {'loans': loans}

    return render(request,'loans_staff.html',context)


########Profiles########
def profile_visitors(request):
    
    context ={}
    persons = Visitor.objects.all()
    header = 'CUSTOMERS'
    context = {'persons':persons , 'header':header}

    if 'del' in request.POST:
        person_id = int(request.POST.get('person'))
        user = User.objects.get(id = person_id)
        user.delete()
    elif 'add' in request.POST:
        return redirect('register')

    return  render(request,'profiles.html',context)

def profile_staff(request):
    
    context ={}
    persons = []

    persons = User.objects.all()
    persons = list(filter(lambda person:person.is_staff,persons))
    header = 'WORKERS'   
    context = {'persons':persons , 'header':header}

    if 'del' in request.POST:
        person_id = int(request.POST.get('person'))
        user = User.objects.get(id = person_id)
        user.delete()
    elif 'add' in request.POST:
        request.session["type"] = "staff"
        return redirect('register')

    return  render(request,'profiles.html',context)




