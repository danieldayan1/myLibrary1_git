from Customers import *
from  Books import *
from  Loans import *
from  datetime import *

class Library():

    def __init__(self):

        self.books =  Books()
        self.customers =  Customers()
        self.loans =  Loans()
###############################################################################################################################################################################################################
    def __str__(self):
        s =f"""{self.books.showBooks()}   {self.customers.showCustomers()}  {self.loans.showLoans()}"""
        return s
##############################################################################################################################################################################################################
    """Function to add loan to library loans .           parameter 1 : new loan customer id .
                                                         parameter 2 : new loan book id.
                                                         parameter 3 : new loan begining date(format-yyyymmdd)."""
    def add_loan(self,cust_id=0,b_id=0,loan_d=0,loan_m=0,loan_y=0):
        try:  
            #chack if book\cutomer  of the new loan exists in library
            if self.books.getBookByID(b_id) == -1 or self.customers.getCustomerByID(cust_id) == -1:
                print("Book\Customer not found in library . Please try again !")

            #chack if the book already loaned
            elif self.loans.getLoan(bookID=b_id) != -1:
                print("book already loand to customer !")

            #else
            else:
                loan_date = datetime(loan_y,loan_m,loan_d).date()
                book_type = self.books.getBookByID(b_id).book_type
                if book_type==1:
                    return_date = loan_date+timedelta(days=10)
                elif book_type == 2:
                    return_date = loan_date+timedelta(days=5)
                else:
                    return_date = loan_date+timedelta(days=2)
                self.loans.addLoan(cust_id,b_id,str(loan_date),str(return_date))
        except:
             print("Wrong loan . Please try again !")
###############################################################################################################################################################################################################
    """Function to add customer to library customers     parameter 1 : new customer name .
                                                         parameter 2 : new customer city .
                                                         parameter 3 : new customer age ."""
    def add_customer(self,name=" " , city=" " , age=0):
        self.customers.addCustomer(name,city,age)
###############################################################################################################################################################################################################
    """Function to add book to library books .           parameter 1 : new book name .
                                                         parameter 2 : new book author .
                                                         parameter 3 : new book published year .
                                                         parameter 4 : new book type (1-3) ."""
    def add_book(self,name=" " , author=" " , pub_year=" "  ,book_type=0):
        self.books.addBook(name , author , pub_year  ,book_type)
###############################################################################################################################################################################################################
    """Function to print library books ."""
    def print_books(self):
        print(self.books.showBooks())
###############################################################################################################################################################################################################
    """Function to print library customers . """
    def print_customers(self):
        print(self.customers.showCustomers())
###############################################################################################################################################################################################################
    """Function to print library loans . """
    def print_loans(self):
        print(self.loans.showLoans())
###############################################################################################################################################################################################################
    """Function to return loan to library . delete the loan from library loans .            parameter 1 : returned loan customer id .
                                                                                            parameter 2 : returned loan book id ."""
    def del_loan(self,cust_id=0,book_id=0):     
        try:
            #chack if loan exists in library
            loan = self.loans.getLoan(cust_id,book_id)
            if loan == -1 :
                print("loan not exists . please try again !")
            else:
                self.loans.delLoan(loan)

        except Exception:
            print("Error accured . Can not return loan . Please try again !")
###############################################################################################################################################################################################################
    """Function to remove book from library books .                                         parameter 1 : delited book id ."""
    def del_book(self,b_id=0):
        try:

            #chack if  book exists in library
            if self.books.getBookByID(b_id) == -1:
                print("book not exists . please try again !")

            #chack if book exists in loans
            elif self.loans.getLoan(bookID=b_id) != -1:
                print("book can not be delited . Loan exists with the same book !")

                #book found   
            else:
                self.books.delBook(b_id)
        except:
                print("book not found in library !")
###############################################################################################################################################################################################################
    """Function to remove customer from library customers .                                 parameter 1 : delited customer id ."""
    def del_customer(self,c_id=0):
        try:

            #chack if customer exists in library
            if self.customers.getCustomerByID(c_id) == -1:
                print("customer not exists . please try again !")

            #chack if customer exists in loans
            elif self.loans.getLoan(custID=c_id) != -1:
                print("Customer can not be delited . Loan exists with the same customer !")

            #customer found
            else:
                self.customers.delCustomer(c_id)

        except:
                print("customer not found in library !")
###############################################################################################################################################################################################################
    """Function to return book details from library books .                                 parameter 1 : request book name ."""
    def find_book(self,name=" "):
        return self.books.getBookByName(name)
###############################################################################################################################################################################################################
    """Function to return customer details from library customers .                         parameter 1 : request customer name ."""
    def find_customer(self,name=" "):
        return self.customers.getCustomerByName(name)
