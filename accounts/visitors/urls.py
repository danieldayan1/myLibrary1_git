
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
    path('add_loan/', add_loan , name = 'add_loan'),
]

