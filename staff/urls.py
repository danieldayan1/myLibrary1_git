
from django.urls import path 
from .views import *


urlpatterns = [
    path('Home_staff/', Home_staff , name = 'Home_staff') , 
    path('carusel_staff/', carusel_staff , name = 'carusel_staff') ,
    path('books_staff/', books_staff , name = 'books_staff') ,
    path('loans_staff/', loans_staff , name = 'loans_staff') ,
    path('profile_visitors/', profile_visitors , name = 'profile_visitors'),
    path('profile_staff/', profile_staff , name = 'profile_staff'),
    path('add_book/', add_book , name = 'add_book'),
]

