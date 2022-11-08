from django.shortcuts import redirect, render, get_object_or_404  , HttpResponse
from django.urls import reverse  
from django.views.decorators.clickjacking import xframe_options_exempt,xframe_options_deny
from django.views.generic import ListView , DetailView
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
def Home_visitors(request):
    context = Home_content(request)
    return render(request,'Home_visitors.html',context)

def Home_staff(request):
    context = Home_content(request)
    return render(request,'Home_staff.html',context)

def Home_content(request):
    context = {'message':'WELCOME TO LIBRARY SITE!!'}
    if request.method=='GET':
        try:
            user = request.user
            context = {'message':f'HI {user} !! WELCOME TO LIBRARY SITE !!'}
        except:
            context = {'message':'WELCOME TO LIBRARY SITE!!'}
    return context

@xframe_options_exempt
def carusel_visitors(request):
    return  render(request,'carusel_visitors.html',{})

@xframe_options_exempt
def carusel_staff(request):
    return  render(request,'carusel_staff.html',{})

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

def books_visitors(request):
    errors = ''
    books = Book.objects.all()
    
    if 'search' in request.GET:
        books = books_search(request,books)
        errors = request.session.get('errors')
        
    context = {'books':books , 'errors':errors}
    return render(request,'books_visitors.html',context)

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

def add_book(request):
    
    errors = ""
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            respnose_cont ='<a href = "/visitors/books_staff"> BOOK ADDED SUCCEFULY ! CLICK HERE TO RETURN TO BOOKS LIST ...</a>'
            return HttpResponse(respnose_cont)
        else:
            errors = form.errors
        
    content = {'form':form,'errors':errors}
    return render(request,'add_book.html',content)


###############loans##############
def loans_visitors(request):
    loans = Loan.objects.filter(customer = request.user.customer).order_by('-borrow_date')
    context = {'loans': loans}

    return render(request,'loans_visitors.html',context)

def loans_staff(request):
    loans = Loan.objects.all().order_by('-borrow_date')
    context = {'loans': loans}

    return render(request,'loans_staff.html',context)

def return_loan(request,loan_id):
    try:
        loan = get_object_or_404(Loan,id = loan_id)
        loan.return_date = datetime.today().date()
        loan.save()

        #chack if books return in time
        if loan.dest_return_date < loan.return_date :
            return HttpResponse("<a href = /visitors/loans_visitors> <h1>books not returned in time ! click here to return to loans list ...</h1></a>")
        else:
            return HttpResponse("<a href = /visitors/loans_visitors><h1>books returned in time ! click here to return to loans list ...</h1></a>")
    except:
        return HttpResponse("<h1>some error accured . please try again .</h1>")

def borrow_loan(request):

    errors = ''
    books = calc_free_books()

    if 'back' in request.GET:
        return redirect('loans_visitors')
    elif 'continue' in request.GET:
        if 'book' in request.GET:
            request.session['books'] = request.GET.getlist('book')

            return redirect('add_loan')
        else:
            errors = 'no books chosen !'
    elif 'search' in request.GET:
        books = books_search(request,books)
        errors = request.session.get('errors')
       
    context = {'books':books , 'errors':errors}
    return render(request,'books_for_loan.html',context)

def add_loan(request):
    l_books_id = request.session['books']
    books = Book.objects.filter(identication__in = l_books_id)
    cust = request.user.customer
    now = datetime.today().date()
    loan = Loan(customer = cust , borrow_date = now )
    loan.save()
    loan.books.set(books)
    return redirect('borrow_loan_details' , pk=loan.id)  


class BorrowLoanDetails(DetailView):
    # slug_field = 'borrow_date'
    # slug_url_kwarg = 'now'
    model = Loan
    template_name = 'borrow_loan_details.html'


##############profiles##############
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
    header = 'WORKERS'   
    context = {'persons':persons , 'header':header}

    if 'del' in request.POST:
        person_id = int(request.POST.get('person'))
        user = User.objects.get(id = person_id)
        user.delete()
    elif 'add' in request.POST:
        return redirect('register')

    return  render(request,'profiles.html',context)



def calc_free_books():

    active_books = []
    free_books = []

    active_loans = Loan.objects.filter(return_date = None)
    active_books = active_loans.values_list('books')
    free_books = Book.objects.exclude(identication__in  = active_books)

    return free_books







