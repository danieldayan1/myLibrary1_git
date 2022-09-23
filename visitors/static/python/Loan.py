from datetime import *

class Loan():

    def __init__(self,cust_id=0,book_id=0,loan_date=" ",return_date=" "):
        if isinstance(cust_id,int) and isinstance(book_id,int) and isinstance(loan_date,str) and isinstance(return_date,str) :
            self.cust_id = cust_id
            self.book_id = book_id
            self.loan_date = loan_date
            self.return_date = return_date
            
    def __str__(self):
        return "customer id:{0} | book id:{1} | loan date:{2} | return date:{3}".format(self.cust_id,self.book_id,self.loan_date,self.return_date)



