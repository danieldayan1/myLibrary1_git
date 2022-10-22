# from django.forms import forms
from .models import *
from django import forms



books = Book.objects.all()
loans = Loan.objects.filter(return_date = None)
active_books = []
free_books = []

#calc active books
for loan in loans:
    for book in books:
        if book in loan.books.all():
            active_books.append(book.name)

#calc free books
free_books = Book.objects.exclude(name__in  = active_books)
free_books_names = list(map(lambda book: book.name , free_books))
free_books_identication = list(map(lambda book: book.identication , free_books))

options = tuple(zip(free_books_identication,free_books_names))

class loansForm(forms.Form):

    books = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=options)
