from django.urls import reverse
from django.db import models
from accounts.models import Visitor
from django.utils import timezone
from datetime import datetime , timedelta
from django.core.validators import MinValueValidator , MaxValueValidator


class Book(models.Model):
    identication = models.CharField(primary_key = True , max_length=50)
    name = models.CharField(max_length=50 , null = True , blank = True)
    author = models.CharField(max_length=50 , null = True , blank = True)
    published_year = models.IntegerField( null = True , blank = True)
    book_type = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)] ,blank=True ,  null = True)

    def __str__(self):
        return f"Title:{self.name} | By Author:{self.author} |  Published In:{self.published_year} | Type:{self.book_type} | id:{self.identication} "


class Loan(models.Model):
    customer = models.ForeignKey(Visitor,on_delete = models.CASCADE)
    book = models.ForeignKey(Book,on_delete = models.CASCADE  , null=True , blank = True )
    borrow_date = models.DateTimeField(auto_now_add=True , blank = True)
    return_date = models.DateTimeField(null=True , blank = True)

    @property
    def dest_return_date(self):
        now = datetime.today().date()
        days=0
        if self.book.book_type == 1:
            days+=10
        elif self.book.book_type == 2:
            days+=5
        else:
            days+=2

        return  now + timedelta(days=days)

    def __str__(self):

        if self.return_date:
            ret_date = f"Return Date: {self.return_date.date()}"
        else:
            ret_date =  "Return Date: Not Return Yet ! "
        
        return f"Customer:{self.customer.slug_name}  | books:{self.book.name} | Borrow Date:{self.borrow_date.date()} | {ret_date} | Destination Return Date:{self.dest_return_date} "
