from django.shortcuts import redirect, render, get_object_or_404  , HttpResponse
from django.urls import reverse  
from django.views.decorators.clickjacking import xframe_options_exempt,xframe_options_deny
from django.views.generic import ListView , DetailView
from django.utils import timezone
from datetime import *

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

def books(request):
    errors = ''
    books = Book.objects.all()
    
    if 'search' in request.GET:
        books = books_search(request,books)
        errors = request.session.get('errors')
        
    context = {'books':books , 'errors':errors}
    return render(request,'books.html',context)


def loans(request):
    loans = Loan.objects.filter(customer = request.user.customer).order_by('-borrow_date')
    context = {'loans': loans}

    return render(request,'loans.html',context)

def return_loan(request,loan_id):
    try:
        loan = Loan.objects.get(id = loan_id)
        loan.return_date = None
        loan.save()

        return_in = calc_return_date_for_loan(loan.books)
        if return_in < datetime.today().date():
            return HttpResponse("<h1>books not returned in time !</h1>")
        else:
            return HttpResponse("<h1>books returned in time !</h1>")
    except:
        return HttpResponse("<h1>some error accured . please try again .</h1>")

def borrow_loan(request):

    errors = ''
    books = calc_free_books()

    #back to loans page
    if 'back' in request.GET:
        return redirect('loans')
    #save loan
    elif 'continue' in request.GET:
        print(request.GET)
        if 'book' in request.GET:
            cust = request.user.customer
            now = datetime.today().date()
            return_in = calc_return_date_for_loan(books)
            books = request.GET.getlist('book')
            loan = Loan(customer = cust , borrow_date = now , return_date = return_in)
            loan.save()
            loan.books.set(books)
            return redirect('borrow_loan_details' , now = datetime.today().date())  
        else:
            errors = 'no books chosen !'
    #search books
    elif 'search' in request.GET:
        books = books_search(request,books)
        errors = request.session.get('errors')
       
    context = {'books':books , 'errors':errors}
    return render(request,'books_for_loan.html',context)

class BorrowLoanDetails(DetailView):
    slug_field = 'borrow_date'
    slug_url_kwarg = 'now'
    model = Loan
    template_name = 'borrow_loan_details.html'




def calc_free_books():

    books = Book.objects.all()
    loans = Loan.objects.exclude(return_date = None)
    active_books = []
    free_books = []

    #calc active books
    for loan in loans:
        for book in books:
            if book in loan.books.all():
                active_books.append(book.identication)

    #calc free books
    free_books = Book.objects.exclude(identication__in  = active_books)
    return free_books

def calc_return_date_for_loan(books):

    now = datetime.today().date()
    days=0
    for book in books:
        if book.book_type == 1:
            days+=10
        elif book.book_type == 2:
            days+=5
        else:
            days+=2

    return  now + timedelta(days=days)
