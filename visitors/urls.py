
from django.urls import path 
from .views import *
from .models import *

urlpatterns = [
    path('Home_visitors/', Home_visitors , name = 'Home_visitors') , 
    path('carusel_visitors/', carusel_visitors , name = 'carusel_visitors') ,
    path('books_visitors/', books_visitors , name = 'books_visitors') ,
    path('loans_visitors/', loans_visitors , name = 'loans_visitors') ,
    path('return_loan/<int:loan_id>', return_loan , name = 'return_loan') ,
    path('borrow_loan/', borrow_loan , name = 'borrow_loan') ,
    path('borrow_loan_details/<int:pk>', BorrowLoanDetails.as_view() , name = 'borrow_loan_details') ,
    path('Home_staff/', Home_staff , name = 'Home_staff') , 
    path('carusel_staff/', carusel_staff , name = 'carusel_staff') ,
    path('books_staff/', books_staff , name = 'books_staff') ,
    path('loans_staff/', loans_staff , name = 'loans_staff') ,
    path('profile_visitors/', profile_visitors , name = 'profile_visitors'),
    path('profile_staff/', profile_staff , name = 'profile_staff'),
    path('add_book/', add_book , name = 'add_book'),
    path('add_loan/', add_loan , name = 'add_loan'),
]

