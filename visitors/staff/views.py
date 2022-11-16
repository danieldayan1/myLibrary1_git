from django.shortcuts import redirect, render, get_object_or_404  , HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt,xframe_options_deny
from datetime import *
from  django.contrib.auth.models import User
from  accounts.models import Visitor
from  visitors.models import Book , Loan
from  accounts.urls import register
from django.views.generic import ListView , DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout

from .models import *
from .forms import *
from .templates import *
from .static import *


##########Home#########
@login_required(login_url='login')
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
        books = books.filter(name__icontains = request.GET.get("name"))
    if request.GET.get("author"):
        books = books.filter(author__icontains = request.GET.get("author"))
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def return_loan(request,loan_id):
    try:
        loan = get_object_or_404(Loan,id = loan_id)
        loan.return_date = datetime.today().date()
        loan.save()

        #chack if books return in time
        if loan.dest_return_date < loan.return_date :
            return HttpResponse("<a href = /staff/loans_staff> <h1>books not returned in time ! click here to return to loans list ...</h1></a>")
        else:
            return HttpResponse("<a href = /staff/loans_staff><h1>books returned in time ! click here to return to loans list ...</h1></a>")
    except:
        return HttpResponse("<h1>some error accured . please try again .</h1>")

@login_required(login_url='login')
def borrow_loan(request):

    errors = ''
    books = calc_free_books()
    form = LoanForm()
    
    if 'search' in request.GET:
        books = books_search(request,books)
        errors = request.session.get('errors')

    elif 'back' in request.POST:
        return redirect('loans_staff')

    elif 'continue' in request.POST:
        if 'book' in request.POST:
            books = Book.objects.filter(identication__in = request.POST.getlist('book'))
            form = LoanForm(request.POST)
            if form.is_valid():
                books = Book.objects.filter(identication__in = request.POST.getlist('book'))
                user =  User.objects.get(id = int( form.cleaned_data['user'])) 
                cust = Visitor.objects.get(user = user)
                now = datetime.today().date()
                for book in books:
                    loan = Loan(customer = cust , borrow_date = now , book = book )
                    loan.save()   
                minute = datetime.today().date() + timedelta(minutes=1)
                return redirect('borrow_loans_details' , now = minute)
            else:
                errors = form.errors
        else:
            errors = 'no books chosen !'

       
    context = {'form':form , 'books':books , 'errors':errors}
    return render(request,'borrow_loan.html',context)

def calc_free_books():

    active_books = []
    free_books = []

    active_loans = Loan.objects.filter(return_date = None)
    active_books = active_loans.values_list('book')
    free_books = Book.objects.exclude(identication__in  = active_books)

    return free_books

class BorrowLoansDetails(ListView):
    slug_field = 'borrow_date'
    slug_url_kwarg = 'now'
    model = Loan
    template_name = 'borrow_loan_details.html'
    paginate_by = 2



########Profiles########
def profile_visitors(request):
    
    context ={}
    persons = Visitor.objects.all()
    header = 'CUSTOMERS'
    context = {'persons':persons , 'header':header}
 
    if 'del' in request.POST:
        person_id = int(request.POST.get('person_id'))
        visitor = Visitor.objects.get(id = person_id)
        user = visitor.user
        user.delete()

    return  render(request,'profiles.html',context)

def profile_staff(request):
    
    context ={}
    persons = []

    persons = User.objects.all()
    persons = list(filter(lambda person:person.is_staff,persons))
    header = 'WORKERS'   
    context = {'persons':persons , 'header':header}
   
    if 'del' in request.POST:
        user_name = request.POST.get('person')
        user = User.objects.get(username = user_name)
        user.delete()
        return redirect('profile_staff')
    elif 'add' in request.GET:
        request.session["entrance_from"] = "staff"
        return redirect('register')

    return  render(request,'profiles.html',context)




