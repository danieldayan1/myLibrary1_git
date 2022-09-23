import  os , csv , io 
from  Loan import *

class Loans():

    def __init__(self):
        self.loans = self.__extract_loans_records()
 
    def __extract_loans_records(self):
        path = input("Type your loan's file . Type any other key for default file: ")
        if (os.path.exists(path))==False:
            path = os.path.join(os.path.dirname(__file__),r'library-loans.csv')
            print(f"wrong file  . choosing from default file: {path}")
    
        with  open(path, 'r') as f:
            csv_reader =  csv.reader(f , delimiter=' ', quotechar='|')

            #create loans records
            loans_list = []
            for line in csv_reader:
                l = line[0].split(",")
                cust_id , book_id , loan_date , return_date = int(l[0]) , int(l[1]) , l[2] , l[3]
                loan = Loan(cust_id,book_id,return_date,loan_date)
                loans_list.append(loan)
            f.close()

        return loans_list
###################################################

    def getLoan(self, custID=0 , bookID= 0):

        for loan in self.loans:
            if (custID == 0 or loan.cust_id == custID)  and (bookID == 0 or loan.book_id == bookID):
                return loan      
        return -1
#####################################################

    def showLoans(self):
        s="______________________________________LOANS________________________________________\n"
        try:
            for loan in self.loans:
                s+= f"{str(loan)} \n"
        except:
            pass
        return s
#####################################################

    def delLoan(self,loan):
        try:
            self.loans.remove(loan)
            print("loan has been returned !")
        except:
            print("wrong loan . please try again !")
########################################################

    def addLoan(self,cust_id,book_id,loan_date,return_date):
        try:
            new_loan = Loan(cust_id , book_id,loan_date,return_date)
            self.loans.append(new_loan)
            print(f"Loan with customer id:{cust_id} and book id:{book_id}  added succefuly !")
        except:
            print("Adding loan failed . Please try again !")
    

