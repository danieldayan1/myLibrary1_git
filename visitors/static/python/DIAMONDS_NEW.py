
import csv , os ,  statistics

"""
This 2 functions extract the data from the file and transform the data to the right type . 
Arguments: path to the file . 
Result : a dictionary with all the lines from the file orgenized as values in the dictionary .
"""
def extract_data(num_rows=0):
    path = input("type your file: ")
    try:
        csv_file = open(path)
    except IOError:
            #default file
        path = os.path.join(os.path.dirname(__file__),r'diamonds.csv')
        print(f"file not found . choose from default file {path} :")
        csv_file = open(path)
    csv_reader = csv.reader(csv_file)
    rows=[]
    columns=[]
    data = {}

    #file lines
    for row in csv_reader:
        rows.append(row)
    #file columns
    columns = list(zip(*rows))
    #build data
    for column in columns:
        data[column[0]] = column[1:] if num_rows==0  else column[1:num_rows]
    
    prepare_data(data)
    return data 
def prepare_data(data):
    
    def transform_column_type(data , col):
        try: #try to transform column to float
            return  list(map(float,data[col]))
        except :
            try:#try to transform column to int
                return  list(map(int,data[col])) 
            except :#try to transform column to str
                return  list(map(str,data[col])) 

    #transform columns type
    for col in data.keys():
        data[col] = transform_column_type(data,col)
###########################################################################################
"""
This func calculate the max value in a specific column from the file.
Arguments: 
1. the dictionary typed in the first 2 funcs .
2. the column from the file who needs to calculated.
Result : the max value of the column
"""
def find_max(data,col):
    try:
        return max(data[col])
    except:
        return 0
###########################################################################################
"""
This func calculate the average value in a specific column from the dictionary.
Arguments: 
1. the dictionary typed in the first 2 funcs .
2. the column from the file who needs to calculated.
result : the average value of the column
"""
def find_avg(data,col):
    try:
        return round(sum(data[col])/len(data[col]),2)
    except:
        return 0
###########################################################################################
"""
This func count how many times sepcific value found in a specific column from the file.
Arguments: 
1. the dictionary typed in the first 2 funcs .
2. the column from the file who needs to calculated.
3. the value to chack in the column .
result : number of times sepcific value found in the column
"""
def find_count_val(data,col,val):
    try:
        return data[col].count(val)
    except:
        return 0
###########################################################################################
"""
This func find how many values found in a specific column from the file.
Arguments: 
1. the dictionary typed in the first 2 funcs .
2. the column from the file who needs to calculated.
result : number of values found in the column
"""
def find_diff_values(data,col):
    try:
        return len(set(data[col]))
    except:
        return 0
###########################################################################################
"""
This func running on the lines from  the file and chack if the values from col1 are equal to specific value ,
And then calculate the median value from col2 found in thus lines .  
Arguments : 
1. the dictionary typed in the first 2 funcs .
2. col1 - the column from the file who his values needs to be compare to the value .
3. col2 - the column from the file who his median needs to be caculated .
4. val - the value needs to compare to col1 values .
reult: The median of col2 corect values
"""
def find_median_by_value(data,col1,col2,val):
    l=[]
    try:
        #build a list from the right col2 values
        for x,y in list(zip(data[col1],data[col2])):
            if x==val:
                l.append(y) 
    
        mid = statistics.median(l)
        return mid
    except:
        return 0
###########################################################################################   
"""
This func running on the lines from  the file and chack how many differnet values in col1 ,
And then calculate the average value from col2 for each type in col1 .  
Arguments : 
1. the dictionary typed in the first 2 funcs .
2. col1 - the column from the file who his values needs to be compare to the value .
3. col2 - the column from the file who his median needs to be caculated .
reult: The average of col2 corect values for each type in col1 .
"""
def find_avg_by_values(data,col1,col2):
    s=''
    try:
        #find col1 differnt types
        for x in list(set(data[col1])):
            l=[]
            #build a list from the right col2 values for each col1 type
            for y,z in list(zip(data[col1],data[col2])):
                if y==x:
                    l.append(z)

            if len(l)>0:
                avg = sum(l)/len(l)
                s+=f'The average {col2} for {col1}:{x} is:{round(avg,2)} \n' 
    except ZeroDivisionError:
        s='no input found . please try again'
    except:
        s = 'general error with the file . please try again.'
    finally:
        return s


