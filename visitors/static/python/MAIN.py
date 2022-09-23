#python C:\Users\c0523140\Desktop\WORK\ALL\MAIN.py

import books1  , CALCULATOR , pyramid , orders , phones , TESTS , DIAMONDSMain ,  ADVANCED

text = """
select the work from the folowing:
1.   BOOKS  (files)
2.   CALCULATOR  (methods)
3.   PYRAMID  (loops)
4.   ORDERS  (files+methods)
5.   PHONES BOOK  (files+lists)
6.   TESTS  (summary+oop)
7.   DIAMONDS(sumarry basic)
8.   ADVANCED
ELSE ...
"""
text_adv = """
select the work from the advanced folowing topics:
1. REGEX
2. NESTED FUNCTIONS (CLOSERS + DECORATOR)
3. GENERATOR + COPY
4. OOP
"""

while True:
    work = input(text)

    match work:
        case '1':
            print("------ BOOKS  (files)------")
            books1.call_books()
        case '2':
            print("------CALCULATOR  (files+methods)------")
            CALCULATOR.call_calculator()
        case '3':
            print('------ PYRAMID  (loops)------')
            pyramid.call_pyramid()
        case '4':
            print('------ ORDERS  (files+methods)------')
            orders.call_orders()
        case '5':
            print('------PHONES BOOK  (files+lists)------')
            phones.call_phobe_book()
        case '6':
            print('------ TESTS  (summary+oop)------')
            TESTS.call_tests()
        case '7':
            print('------ DIAMONDS(sumarry basic)------')
            DIAMONDSMain.call_diamonds()
        case '8':
            print('------ADVANCED------')
            work_adv =int(input(text_adv))
            match work_adv:
                case 1:
                    print('------REGEX------')
                    ADVANCED.phone_validate()
                    print('-------------')
                    ADVANCED.mail_validate()
                    print('-------------')
                    ADVANCED.replace_nums_regex()
                case 2:
                    print('------NESTED FUNCTIONS (CLOSERS + DECORATOR)------')
                    ADVANCED.call_printmsg1()
                    print('-------------')
                    ADVANCED.call_printmsg2()
                    print('-------------')
                    ADVANCED.call_genfilterby()
                    print('-------------')
                    ADVANCED.call_wraper_adding_stars()
                case 3:
                    print('------GENERATOR + COPY------')
                    ADVANCED.call_print_random_num()
                case 4:
                    print('--------OOP--------')
                    ADVANCED.call_Rectangle()
                    print('-------------')
                    ADVANCED.call_MyStrings()
                    print('-------------')
                    ADVANCED.call_zoo()
                case _:
                    print("return to main menu ...")
                    continue
        case _: 
            input("Type any key for exit ...")
            break