#python C:\Users\c0523140\Desktop\WORK+\ALL\ADVANCED.py
import re , functools , random , copy 
from abc import abstractmethod , ABCMeta

"""
REGEX
"""
def phone_validate():
    phone = input("write your phone: ")
    pattern2 = r"^(\d{3}-)(\d{7})$"
    pc = re.compile(pattern2)
    m = pc.match(phone)
    if m:
        print("ok "+m[1]+" "+m[2])
    else:
        print("wrong")
def mail_validate():

    mail = input("write your web: ")
    patern = r'^(http|https|ftp)://(.*)(\.com)$'
    m = re.search(patern,mail)
    if m:
        print("yes")
    else:
        print("no")
def replace_nums_regex():
    s = "i have 3 books and 4 bags , so give me 5 !"
    nums = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
    new_s = re.sub(r"(\d)",lambda m:nums[int(m.group(1))],s)
    print(f"SENTENCE BEFORE REGEX REPLACE: {s} ")
    print(f"SENTENCE AFTER REGEX REPLACE: {new_s} ")

"""
NESTED FUNCTIONS
"""
def printmsg1(msg,style):

    def print_stars():
        print("********")

    def print_eq():
        print("========") 

    if msg=='*':
        return print_stars
    return print_eq
def call_printmsg1():
    try:
        msg , style = input("type your message and style: ").split(" ")
    except:
        msg , style = "hello","*"
    my_print_func = printmsg1(msg,style)
    my_print_func()
    print(msg)
    my_print_func()

def printmsg2(msg,style):
    #CLOSER
    def print_style():
        print(style*4)

    return print_style
def call_printmsg2():
    try:
        msg , style = input("type your message and style: ").split(" ")
    except:
        msg , style = "hello","*"
    my_print_func = printmsg2(msg,style)
    my_print_func()
    print(msg)
    my_print_func()

def genfilterby(num):
    def inner(t):
        return list(filter(lambda x:x%num==0,t)) 
    return inner
def call_genfilterby():
    fil=genfilterby(3)
    z=[2,3,4,5,6,7,8] 
    print(f"return calc func for: {z} is: ",fil(z))

def wraper_adding_stars(style):
    #DECORATOR
    @functools.wraps(my_adding_stars)
    def inner(s):
        print(style*6)
        my_adding_stars(s) 
        print(style*6)
    return inner
def my_adding_stars(s):
    print(s)
def call_wraper_adding_stars():
    adding_stars = wraper_adding_stars('*')
    adding_stars("hello")

"""
GENERATOR + COPY
"""
def print_random_num(n):
    for i in range(n):
        x = random.randint(0,n)
        yield x 
def call_print_random_num():
    generator = print_random_num(20)
    l1 = [x for x in generator] 
    l2 = copy.deepcopy(l1)
    l1.append([1,2,3])
    print(f"l1  - {l1}")
    print(f"l2 - l1 copy - {l2}")


"""
OOP
"""
class Rectangle(object):

    __counter = 0

    def __init__(self,w=0,h=0,):
        self.__width = w
        self.__height = h
        Rectangle.__counter+=1

    def SetSize(self,w=0,h=0):
        self.__width = w
        self.__height = h

    def __str__(self):
        return f"Rectangle width is:{self.__width} and height:{self.__height}"

    @staticmethod
    def get_counter():
        return Rectangle.__counter
class RoundRectangle(Rectangle):
    def __init__(self,w,h,a):
        super().__init__(w,h)
        self.__angle = a
    
    def SetAngle(self,a):
        self.__angle=a

    def __str__(self):
        s = super().__str__()+f" and angle:{self.__angle}"
        return s
def call_Rectangle():
    r1 = Rectangle(20,10)
    r2 = Rectangle(15,15)
    r3 = RoundRectangle(10,20,30)
    r1.SetSize(20,20)
    print(r1)
    print(r2)
    print(r3)
    print("num of Rectangles objects is:",Rectangle.get_counter())

class MyString():     
    def __init__(self,text):
        self.__text = text
                      
    def __str__(self):
        return self.__text
    
    def __add__(self,string2):
        s=self.__text+"-"+string2.__text
        return MyString(s)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self,t):
        self.__text =t 
class MyStringAbs(metaclass = ABCMeta):     
    def __init__(self,text):
        self.__text = text
    
    @abstractmethod
    def __add__(self,string2):
        pass

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self,t):
        self.__text =t 
class MyStringEx(MyStringAbs):     

    def __init__(self,t):
        super().__init__(t)

    def __add__(self, other):   
        string =   MyStringEx(self._MyStringAbs__text+ '*' + other._MyStringAbs__text)
        string = re.sub('-','*',string._MyStringAbs__text)
        return string

    def __str__(self):
        return self._MyStringAbs__text
def call_MyStrings():
    s1 = MyString("I") 
    s2 = MyString("Love") 
    s3 = MyString("Python") 
    s4 = s1+s2+s3 

    s5 = MyStringEx(str(s4))
    s6 = MyStringEx('Ex')
    #setter
    s6.text = 'Extra'
    s7 = s5+s6
     
    [print(s) for s in [s4,s7]]

class zoo(object):

    def __init__(self,n):
        if isinstance(n,str):
            self.name = n
        self.__animals = []

    def add_animal(self,animal):
        if isinstance(animal,str):
            self.__animals.append(animal)

    @property
    def animals(self):
        return self.__animals

    @animals.setter
    def animals(self,a):
        self.__animals = a

    def sell_animal(self,animal_sold):
        if animal_sold in self.__animals:
            self.__animals.remove(animal_sold)

    def sort_animals(self):
        self.__animals.sort(key=lambda a: a[0])
def call_zoo():
    z = zoo('rishon zoo')
    z.add_animal("Ape")
    z.add_animal("Cat")
    z.add_animal("Bear")
    z.add_animal("Emu")
    z.sort_animals()

    print(z.__dict__)



