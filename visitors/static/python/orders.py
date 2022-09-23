import os

def getCustomerID(name):
    cust_id = " "
    path = input("please type customers file: ")
    try:
        cust_file = open(path)
    except IOError:
        #default file
        path = os.path.join(os.path.dirname(__file__),r'Cust.csv')
        print(f"file not found . choose from default file {path} :")
        cust_file = open(path)
    
    line = cust_file.readline()
    while len(line)>0 :
        l = line.split(",")
        if l[1]==name:
            cust_id = l[0]
            break
        line = cust_file.readline()
    cust_file.close()
    
    return cust_id

def getOrders(cust_id):
    orders = []
    path = input("please type orders file: ")
    try:
        orders_file = open(path)
    except IOError:
        #default file
        path = os.path.join(os.path.dirname(__file__),r'Orders.csv')
        print(f"file not found . choose from default file {path} :")
        orders_file = open(path)
    
    line = orders_file.readline()
    while len(line)>0 :
        l = line.split(",")
        if l[1]==cust_id:
            orders.append(l[3])
        line = orders_file.readline()
    orders_file.close()

    return orders

def output_sum(list1):
    result=0
    list2 = list(map(int,list1))
    for i in range(0,len(list2)) :
        result = result + list2[i]
    print("Total orders: {0}$".format(result))
    

def call_orders():
    name = input("please type the customer name . Else to exit: ")
    while len(name) >0 :
        cust_id= getCustomerID(name)
        if len(cust_id) >0:
            orders_list = getOrders(cust_id)
            if len(orders_list) >0 :
                output_sum(orders_list)
            else:
                print("no orders found ! TRY AGAIN !")  
        else:
            print("WRONG NAME ! TRY AGAIN !")   
        name = input("please type the customer name: ")
    else:
       input("Type any key to exit ... ")

