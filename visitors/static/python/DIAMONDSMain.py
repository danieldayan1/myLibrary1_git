
from DIAMONDS_NEW import *

def call_diamonds():

    data = extract_data()

    print(f"1.max price: {find_max(data,'price')}")
    print(f"2.average price: {find_avg(data,'price')}")
    print(f"3.number of Ideal diamonds: {find_count_val(data,'cut','Ideal')}")
    print(f"4.number of colors: {find_diff_values(data,'color')}")
    print(f"5.The median carat for PREMIUM diamonds is: ",find_median_by_value(data,'cut','carat','Premium'))
    print(f"6.",find_avg_by_values(data,'cut','carat'))
    print(f"7.",find_avg_by_values(data,'color','price'))

