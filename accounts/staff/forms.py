# from django.forms import forms
from visitors.models import *
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'