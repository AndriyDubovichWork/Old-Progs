""" 
    calculator of geometry progrsion of money profit
    python 3.9.5
    windows 10
"""
import os
# def to clear cmd when i need it
def clear():os.system('CLS')

# input all numbers
# input start invested sum
while True:
    number = input("Enter number:")
    if number.isdigit():
        number=int(number)
        break
    else:
        clear()
        print("error")
# input precent of sum what will be add every time intervar
while True:
    precent = input("Enter precent:")
    
    try:
        precent=float(precent)
        
    except:
        clear()
        print("error")
        
    if type(precent)==float:
        precent=float(precent)
        break
# input all time wich you hold your investments
while True:
    days = input("Enter number of month:")
    if days.isdigit():
        days=int(days)
        break
    else:
        clear()
        print("error")
# input number of money wich you add every time interval
while True:
    addeable_sum = input("Enter sum what you add every month:")
    if addeable_sum.isdecimal():
        addeable_sum=float(addeable_sum)
        break
    else:
        clear()
        print("error")

i = 0
invested = number
res=0
profit=0
#calculate 
while i<days:
    # calculate precent of all money
    num = (number/100)*precent
    # add number to calculate profit ,invested money
    # increase all money with profit money
    number+=num
    # calculate profit
    profit+=num
    # increase investment to all money every time interval
    if i!=0:
        number+=addeable_sum
        invested+=addeable_sum
    i+=1


# calculate clear profit without investment
profit=number-invested
clear()
# print
print("invested:"+str("%.2f" %invested))
print("profit:"+str("%.2f" %profit))
print("sum:" + str("%.2f" % number))

input()
clear()

