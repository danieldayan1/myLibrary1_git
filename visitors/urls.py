
from django.urls import path 
from .views import *

urlpatterns = [
    path('Home/', Home , name = 'Home') , 
    path('carusel/', carusel , name = 'carusel') ,
]

