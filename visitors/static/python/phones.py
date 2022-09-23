import os

def call_phobe_book():
    phone_book = {}
    path = input("write path for file: ")
    while(True):
        try:
            file = open(path)
        except IOError:
            #default file
            path = os.path.join(os.path.dirname(__file__),r'phones.csv')
            print(f"file not found . choose from default file {path} :")
            file = open(path)
            
        line = file.readline()
        while(len(line)>0):
            list1 = line.split(",")
            if list1[0]=='phone':
                phone_book[list1[1]]=list1[2]
            elif list1[0]=='request':
                if list1[1] in phone_book.keys():
                    print("the request number of {0} is {1}".format(list1[1],phone_book[list1[1]]))
                else:
                    print("unknown number !")
            elif list1[0]=='del':
                if list1[1] in phone_book.keys():
                    del phone_book[list1[1]]
                    print("number deleted !")
                else:
                    print("unknown number !")
            elif list1[0]=='exit':
                break
            line = file.readline()
        break
    input("type any key to exit...")
            
    
    
