from django.forms import forms
from .models import Loan , Book
from django import forms

class LoanForm(forms.Form):

    books = forms.TypedChoiceField(required = True)

    def __init__(self, *args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)

        active_books = []
        free_books = []
        active_loans = Loan.objects.filter(return_date = None)
        active_books = active_loans.values_list('books')
        free_books = Book.objects.exclude(identication__in  = active_books).values_list("identication","name")
      
        self.fields['books'] = forms.TypedChoiceField(choices = free_books , required = True)

