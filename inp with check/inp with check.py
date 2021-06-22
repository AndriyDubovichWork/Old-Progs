
import os




def clear():os.system('CLS')
def get_nums():
    while True:
        first = input("Enter first number:")
        if first.isdigit():
            first=int(first)
            break
    
        clear()
        print("Error")
    while True:
        second = input("Enter second number:")
        if second.isdigit():
            second=int(second)
            break
        clear()
        print("Error")

get_nums()



clear()
