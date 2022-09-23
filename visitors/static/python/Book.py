class Book():

    book_id=9998
    
    def __init__(self,name=" ",Author=" ",published_year=0,book_type=0):
        if isinstance(name,str) and isinstance(Author,str) and isinstance(published_year,int) and (isinstance(book_type,int) and int(book_type) in range(1,4)):
            self.id = Book.book_id
            self.name = name
            self.Author = Author
            self.published_year = published_year
            self.book_type = book_type
            Book.book_id+=1
        else:
            print("error accured with one of the book's details . Please try again !")

    def __str__(self):
        return " ID:{0} | Name:{1} | Author:{2} | Published year:{3} | Book type:{4}".format(self.id,self.name,self.Author,self.published_year,self.book_type)
     