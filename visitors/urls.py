
from django.urls import path 
from .views import *
from .models import *

urlpatterns = [
    path('Home/', Home , name = 'Home') , 
    path('carusel/', carusel , name = 'carusel') ,
    path('books/', books , name = 'books') ,
    path('loans/', loans , name = 'loans') ,
    path('return_loan/<int:loan_id>', return_loan , name = 'return_loan') ,
    path('borrow_loan/', borrow_loan , name = 'borrow_loan') ,
    path('borrow_loan_details/<slug:now>', BorrowLoanDetails.as_view() , name = 'borrow_loan_details') ,
]

