
from DIAMONDS_NEW import *
import pprint

p = pprint.PrettyPrinter(indent=4)
data = {} 
f =input("type your file: ")

"""
Test extract_data function
"""
def TEST_extract_data():
    #right
    data = extract_data(f,10)
    p.pprint(data)
    #wrong
    data = extract_data('no file exists')
    p.pprint(data)
#################################
"""
Test find_max function
"""
def TEST_find_max():
    data = extract_data(f,10)
    
    #right
    print(find_max(data,'price'))
    #wrong
    print(find_max(data,'some_input'))
##################################
"""
test find_avg function
"""
def TEST_find_avg():
    data = extract_data(f,10)
    
    #right
    print(find_avg(data,'price'))
    #wrong
    print(find_avg(data,'some_input'))
##################################
"""
Test find_count_val function
"""
def TEST_find_count_val():
    data = extract_data(f,10)
    
    #right
    print(find_count_val(data,'cut','Ideal'))
    #wrong
    print(find_count_val(data,'INPUT1','Ideal'))
    print(find_count_val(data,'cut','INPUT2'))
##################################
"""
Test find_median_by_value function
"""
def TEST_find_median_by_value():
    data = extract_data(f,10)
    
    #right
    print(find_median_by_value(data,'cut','carat','Premium'))
    #wrong
    print(find_median_by_value(data,'input1','carat','Premium'))
    print(find_median_by_value(data,'cut','input2','Premium'))
    print(find_median_by_value(data,'cut','carat','input3'))
##################################    
"""
Test find_avg_by_values function
"""
def TEST_find_avg_by_values():
    data = extract_data(f,10)
    
    #right
    print(find_avg_by_values(data,'cut','carat'))
    #wrong
    print(find_avg_by_values(data,'input1','carat'))
    print(find_avg_by_values(data,'cut','input2'))




TEST_extract_data()
TEST_find_max()
TEST_find_avg()
TEST_find_count_val()
TEST_find_median_by_value()
TEST_find_avg_by_values()