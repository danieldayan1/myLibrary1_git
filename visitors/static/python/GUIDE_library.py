# python C:\Users\c0523140\Desktop\WORK\ALL\GUIDE_Library.py
from  Library import *
from Customers import *
from  Books import *
from  Loans import *



def add_customer():
    name = input("Type new customer's name: ")
    city = input("city: ")
    age = int(input("age: "))
    library.add_customer(name , city , age)

def add_book():
    name = input("Type new book's name: ")
    author = input("author: ")
    pub_year = int(input("published year: "))
    book_type = int(input("type: "))
    library.add_book(name , author , pub_year  ,book_type)

def add_loan():
    cust_id = int(input("Type new loan's customer ID (format: Number): "))
    book_id = int(input("book ID (format: Number): "))
    loan_date_day , loan_date_month , loan_date_year  =  input("loan date (format: Day Month and Year): ").split(" ")
    library.add_loan(cust_id , book_id , int(loan_date_day) , int(loan_date_month) , int(loan_date_year))

def return_loan():
    cust_id = int(input("To return a loan to the library please type your ID (format: Number): "))
    book_id = int(input("book ID (format: Number): "))
    library.del_loan(cust_id , book_id)

def print_custs():
    library.print_customers()

def print_books():
    library.print_books()

def print_loans():
    library.print_loans()

def find_book():
    name = input("write book name for more details: ")
    print(library.find_book(name))

def find_customer():
    name = input("write customer name for more details: ")
    print(library.find_customer(name))

def delete_book():
    b_id = int(input("write book id to delete: "))
    library.del_book(b_id)

def delete_customer():
    c_id = int(input("write customer id to delete: "))
    library.del_customer(c_id)


###############################   START HERE ################################

library = Library()

add_customer()
add_book()
add_loan()
return_loan()
print_books()
print_custs()
print_loans()
find_book()
find_customer()
delete_book()
delete_customer()

print(library)
