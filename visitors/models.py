from django.urls import reverse
from django.db import models
from accounts.models import Visitor
from django.utils import timezone

class Book(models.Model):
    identication = models.CharField( primary_key = True , max_length=50)
    name = models.CharField(max_length=50 , null = True , blank = True)
    author = models.CharField(max_length=50 , null = True , blank = True)
    published_year = models.IntegerField( null = True , blank = True)
    book_type = models.IntegerField( null = True , blank = True)

    def __str__(self):
        return f"Title:{self.name} | By Author:{self.author} |  Published In:{self.published_year} | Type:{self.book_type} | id:{self.identication} "


class Loan(models.Model):
    customer = models.ForeignKey(Visitor,on_delete = models.CASCADE)
    books = models.ManyToManyField(Book,related_name='loans')
    borrow_date = models.DateField(default=timezone.now , blank = True)
    return_date = models.DateField(null=True , blank = True)

    def __str__(self):
        books = self.books.all()
        books_names = ''
        for book in books:
            books_names+=book.name+' , '
        books_names = books_names[:len(books_names)-2] 
        
        return f"Customer:{self.customer.first_name} {self.customer.last_name} | books:{books_names} | Borrow Date:{self.borrow_date} | Return Date:{self.return_date} "
