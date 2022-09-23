def calc_reg(*args):
    result = 0
    if args[2]==r'+':
        result = args[0] + args[1]
    elif args[2]==r'-':
        result = args[1]-args[0] if args[0]<args[1] else args[0]-args[1]
    elif args[2]==r'*':
        result = args[0]*args[1]
    elif args[2] == '\\':
        result = args[1]/args[0] if args[0]<args[1] else args[0]/args[1]
    elif args[2]==r'^':
        result = pow(args[0],args[1])
    return result

def output_screen():
        s = input("Write your excercises . Else to exit : ")
        num1 = int(s[0])
        operator = s[1]
        num2 = int(s[2])

        try:
            while True:
                result = calc_reg(num1,num2,operator)
                print(f"{result}" )
                s = input("")
                num1 = int(s[0]) 
                operator = s[1]
                num2 = int(s[2])
        except:
            print("END")

def call_calculator():
    output_screen()