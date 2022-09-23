class Customer():

    cust_id=110

    def __init__(self,name=" ",city=" ",age=0):
        if isinstance(name,str) and isinstance(city,str) and isinstance(age,int) :
            self.id = Customer.cust_id
            self.name = name
            self.city = city
            self.age = age
            Customer.cust_id += 1
        else:
            print("error accured with one of the book's details . Please try again !")

    def __str__(self):
        return f"id:{self.id} | name:{self.name} | city:{self.city} | age:{self.age}"