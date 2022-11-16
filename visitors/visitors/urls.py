
from django.urls import path 
from .views import *
from .models import *

urlpatterns = [
    path('Home_visitors/', Home_visitors , name = 'Home_visitors') , 
    path('carusel_visitors/', carusel_visitors , name = 'carusel_visitors') ,
    path('books_visitors/', books_visitors , name = 'books_visitors') ,
    path('loans_visitors/', loans_visitors , name = 'loans_visitors') ,
]

