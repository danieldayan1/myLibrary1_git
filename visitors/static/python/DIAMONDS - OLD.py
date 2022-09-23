#python C:\Users\c0523140\Desktop\WORKS\DIAMONDS\DIAMONDS.py   C:\Users\c0523140\Desktop\WORKS\DIAMONDS\diamonds.csv
import csv,os

""" 
1. find the max prise of the diamonds in file
"""
def max_prise(rows):
    max=0
    for row in rows:
        if int(row[6])>max:
            max=int(row[6])
    return max

""" 
2. find the average prise of the diamonds in file
"""
def avg_prise(rows):
    avg = 0
    sum=0
    for row in rows:
        sum+=int(row[6])
    try:
        avg = sum/len(rows)
    except ZeroDivisionError:
        print("found 0 lines in file . please try again . ")

    return round(avg,2)

"""
3. find number of IDEAL diamonds in file
"""
def find_ideal(rows):
    list_ideal = list(filter(lambda row: row[1]=='Ideal',rows))
    return len(list_ideal)

"""
4. find number of colors in file
"""
def find_diff_color(rows):
    set_colors=set()
    for row in rows:
        set_colors.add(row[2])
    return len(set_colors)

"""
5. find middle carat of PREMIUM diamonds in file
"""
def find_premium_mid(rows):
    list_premium = []
    for row in rows:
        if row[1] == "Premium":
            list_premium.append(row[0])
    if len(list_premium)!=0:
        list_premium.sort()
        return list_premium[int(len(list_premium) / 2)]
    return 0

"""
6. find the average carat of every cut in file
"""
def find_cut_avg_carat(rows):
    result=''
    #create list of the cuts
    set_cuts=set()
    for row in rows:
        set_cuts.add(row[1])
    l_cuts = list(set_cuts)

    #calculate avg carat for every cut in l_cuts
    for cut in l_cuts:
        sum=0
        counter=0
        avg=0
        for row in rows:
            if row[1] == cut :
                sum+=float(row[0])
                counter+=1
        try:
            avg = sum/counter
            result+='the avg carat of diamond cut: {0} is: {1} \n'.format(cut,round(avg,2))
        except ZeroDivisionError:
            continue
    return result

"""
7. find the average prise of every color in file
"""
def find_color_avg_prise(rows):
    result=''
    #create list of the colors
    set_colors=set()
    for row in rows:
        set_colors.add(row[2])
    l_colors = list(set_colors)

    #calculate avg prise for every color in l_colors
    for myColor in l_colors:
        sum=0
        counter=0
        avg=0
        for row in rows:
            if row[2] == myColor :
                sum+=int(row[6])
                counter+=1
        try:
            avg = sum/counter
            result+='the avg prise of diamond color: {0} is: {1} \n'.format(myColor,round(avg,2))
        except ZeroDivisionError :
            continue
    return result
            
#MAIN
while True:

    fields = []
    rows = []
    path = input("please write your file : ")
    if not(os.path.exists(path)):
                print("file not exists . please try again !")
    else:
        try:
            with open(path,'r') as csvfile:
                    csvreader = csv.reader(csvfile)
                    #file header
                    fields = next(csvreader)
                    #file lines
                    for row in csvreader:
                        rows.append(row)
                        
                    print('max price for diamond is: {0}'.format(max_prise(rows)))
                    print('avg price for diamond is: {0}'.format(avg_prise(rows)))
                    print('num of IDEAL diamonds in total is:{0}'.format(find_ideal(rows)))
                    print('num of differnt color is:{0}'.format(find_diff_color(rows)))
                    print('middle value of PREMIUM diamonds is:{0}'.format(find_premium_mid(rows)))
                    print(find_cut_avg_carat(rows))
                    print(find_color_avg_prise(rows))
                    csvfile.close()
        except:
            print("there are some problems with the file . \n")
        if(input("enter any key for run programe again . EXIT otherwise : ").upper()=='EXIT'):
            break