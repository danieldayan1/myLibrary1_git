# from django.forms import forms
from visitors.models import *
from django import forms
from  django.contrib.auth.models import User

class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # Making location required
        self.fields['name'].required = True
        self.fields['author'].required = True
        self.fields['published_year'].required = True
        self.fields['book_type'].required = True

    class Meta:
        model = Book
        fields = '__all__'



class LoanForm(forms.Form):

    # books = forms.TypedChoiceField(required = False)
    user = forms.TypedChoiceField( required = True)

    def __init__(self, *args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)

        active_books = []
        free_books = []
        active_loans = Loan.objects.filter(return_date = None)
        active_books = active_loans.values_list('book')
        free_books = Book.objects.exclude(identication__in  = active_books).values_list("identication","name")
      
        self.fields['books'] = forms.TypedChoiceField(choices = free_books , required = False)

        users = Visitor.objects.all().values_list("user" , "name")
        self.fields['user'] = forms.TypedChoiceField(choices = users , required = True)
