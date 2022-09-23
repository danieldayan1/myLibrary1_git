import os

def call_books():
    try:
        path = input("write path for file: ")
        try:
            file = open(path)
        except IOError:
            #default file
            path = os.path.join(os.path.dirname(__file__),r'books.txt')
            print(f"file not found . choose from default file {path} :")
            file = open(path)
        name = " "
        year = 0
        money = 0
        pay_on_time = False
        dic = {}
        line = file.readline()
        while(len(line)>0):
            list1 = line.split(" ")
            name = list1[0]
            year = list1[1]
            money = list1[2]
            pay_on_time = True if list1[3]==list1[1] else False
            dic[name] = [year,money,pay_on_time]
            line = file.readline()
        for key in dic:
            if dic[key][2]== True and int(dic[key][1])>=8000:
                print("customer:{0}  is: VIP".format(key))
            else:
                print("cutomer:{0}  is REGULAR".format(key))
        file.close()
    except:
        print("something wrong with the file")
    finally:
        input("press any key to continue ... ")

