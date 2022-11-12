import os
import django
import random 
from visitors.models import Book , Loan
from accounts.models import Visitor
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myLibrary.settings')
django.setup()



# def create_users(n):

#     for i in range(1,n):
#         created=False
#         while not created:
#             try:
#                 user = User(name=f'name{i}',password=i)
#                 user.save()
#                 identication = i
#                 visitor = Visitor(user=user,identication=identication)
#                 visitor.save()
#                 created= True
#             except:
#                 continue

# def create_books():
 
#     response = request.get('https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes')
#     bookapi = response.json()['items']

#     for book,i in zip(enumerate(bookapi)):
#         created=False
#         while not created:
#             try:
#                 identication = i
#                 name = book[i]['volumeInfo']['title']
#                 author = book[i]['volumeInfo']['authors'][0]
#                 published_year = book[i]['volumeInfo']['publishedDate'][:4]
#                 b = Book(identication=identication,name=name,author=author,published_year=published_year, book_type = random.randint(1,3))
#                 b.save()
#                 created= True
#             except:
#                 continue


# if __name__ == '__main__':
#     print("Populating database")
#     create_users(5)
#     create_books()