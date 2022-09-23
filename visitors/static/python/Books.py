import  os , csv , io 
from  Book import *

class Books():

    def __init__(self):
        self.books = self.__extract_books_records()

    def __extract_books_records(self):
        path = input("Type your book's file . Type any other key for default file: ")
        if (os.path.exists(path))==False:
            path = os.path.join(os.path.dirname(__file__),r'library-books.csv')
            print(f"Wrong file  . Choosing from default file: {path}")
        
        with  open(path, 'r') as f:
            csv_reader = csv.reader(f , delimiter=' ', quotechar='|')
        #create books records
            books_list = []
            for line in csv_reader:
                l=line[0].split(",")
                name , author , pub_year  ,book_type = l[0] , l[1] , int(l[2]) , int(l[3])
                book = Book(name , author , pub_year , book_type)
                books_list.append(book)
            f.close()

            return books_list
#######################################################

    def getBookByID(self,myID):
        try:
            for book in self.books:
                if book.id == myID:
                    return book
            return -1
        except:
            return -1
########################################################

    def getBookByName(self,n=" "):
        try:
            for book in self.books:
                if book.name.upper() == n.upper():
                    return book
            return "no book found !"
        except:
            return "no book found !"
####################################################
 
    def showBooks(self):
        s=f"____________________________________BOOKS________________________________________\n"
        try:
            for book in self.books:
                s+= f"{str(book)} \n"
        except:
            pass
        return s
#######################################################

    def addBook(self,name=" " , author=" " , pub_year=" "  ,book_type=0):
        try:
            new_book = Book(name,author,int(pub_year),int(book_type))
            self.books.append(new_book)
            print(f"Book id: {new_book.id} added succefuly !")
        except:
            print("Adding book failed . Please try again !")
###########################################################

    def delBook(self,b_id=0):
        try: 
            #chack if book exists in library
            book = self.getBookByID(b_id)
            if book != -1:
                self.books.remove(book)
                print("book delited !")
            else:
                print("book not found in library !")
        except:
            print("wrong book . please try again !")



