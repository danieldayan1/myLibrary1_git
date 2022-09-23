def call_pyramid():
    num = int(input("write your number: "))
    if num>0:
        for row in range(num):
            #spaces
            for j in range(num-row-1):
                print(" ", end="")
            #stars
            for k in range(row*2+1):
                print('*',end="")
            print()
    else:
        print("wrong number! ")
    input("press any key to exit...")


