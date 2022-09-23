# python C:\Users\c0523140\Desktop\WORK\ALL\TESTS_Library.py
from  Library import *
from Customers import *
from  Books import *
from  Loans import *




def test_add_cust():
    
    #right
    print("RIGHT")
    library.add_customer("aaa" , "haifa" , 10)
    
    #wrong
    print("WRONG")
    library.add_customer("aaa" , 123 , 10)

def test_add_book():
    
    #right
    print("RIGHT")
    library.add_book("sss" , "dan" , 2010  ,1)
    
    #wrong
    print("WRONG")
    library.add_book("aaa" , 123 , 10 , 4)

def test_add_loan():
    
    #right
    print("RIGHT")
    library.add_loan(111 , 9998 , 1 , 1 , 2022 )
    
    #wrong
    print("WRONG")
    library.add_loan(111 ,123456789 , 1 , 1 ,  2022 ) 
    library.add_loan(789 ,9999 , 1 ,1 , 2022 )
    library.add_loan(112 ,9999 , 1 , 1 , 2022 )

def test_return_loan():

    #right
    print("RIGHT")
    library.del_loan(111 , 9999)

    #wrong
    print("WRONG")
    library.del_loan(112 , 9999)
    library.del_loan(111 , '684681681')

def test_find_book():

    #right
    print("RIGHT")
    print(library.find_book("table"))

    #wrong
    print("WRONG")
    print(library.find_book("llkjlkj"))

def test_find_customer():

    #right
    print("RIGHT")
    print(library.find_customer("bla"))

    #wrong
    print("WRONG")
    print(library.find_customer("llkjlkj"))

def test_del_book():

    #right
    print("RIGHT")
    library.del_book(9999)

    #wrong
    print("WRONG")
    library.del_book(651651351)
    library.del_book(9998)

def test_del_customer():

    #right
    print("RIGHT")
    library.del_customer(110)

    #wrong
    print("WRONG")
    library.del_customer(365135135)
    library.del_customer(112)



library = Library()

test_add_cust()
test_add_book()
test_add_loan()
test_return_loan()
test_find_book()
test_find_customer()
test_del_book()
test_del_customer()



