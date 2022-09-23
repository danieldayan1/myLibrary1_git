import  os , csv , io 
from  Customer import *

class Customers():

    def __init__(self):
        self.customers = self.__extract_customers_records()
 
    def __extract_customers_records(self):
        path = input("Type your book's file . Type any other key for default file: ")
        if (os.path.exists(path))==False:
            path = os.path.join(os.path.dirname(__file__),r'library-books.csv')
            print(f"Wrong file  . Choosing from default file: {path}")
        
        with  open(path, 'r') as f:
            csv_reader = csv.reader(f , delimiter=' ', quotechar='|')
        #create books records
            customers_list = []
            for line in csv_reader:
                l=line[0].split(",")
                name , city , age = l[0] , l[1] , int(l[2])
                customer = Customer(name , city , age)
                customers_list.append(customer)
            f.close()

            return customers_list
#########################################################

    def getCustomerByID(self, myID):
        try:
            for customer in self.customers:
                if customer.id == myID:
                    return customer
            return -1
        except:
            return -1
##########################################################

    def getCustomerByName(self, name):
        try:
            for customer in self.customers:
                if customer.name.upper() == name.upper():
                    return customer
            return "no customer found !"
        except:
            return "no customer found !"
#######################################################

    def showCustomers(self):
        s=f"____________________________________CUSTOMERS________________________________________\n"
        try:
            for customer in self.customers:
                s+= f"{str(customer)} \n"
        except:
            pass
        return s
#########################################################
 
    def addCustomer(self,name =" ",city=" ",age=0):
        try:
            new_cust = Customer(name,city,int(age))
            self.customers.append(new_cust)
            print(f"Customer id: {new_cust.id} added succefuly !")
        except:
            print("Adding customer failed . Please try again !")
#########################################################

    def delCustomer(self,c_id=0):
        try:
            customer = self.getCustomerByID(c_id)
            self.customers.remove(customer)
            print("Customer delited !")
        except:
            print("wrong customer . please try again !")




