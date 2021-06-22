import os



# helpful clear for cmd
def clear():os.system('CLS')


#input with check
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
    res = [first,second]
    return res





#rewring nums
nums = get_nums()
a=nums[0]
b=nums[1]


#find NSD


while b>0:
    a,b = b,a%b

NSD=a
NSK=(nums[0]*nums[1])/NSD


clear()
print("NSD = "+str(NSD))
print("NSK = "+str(NSK))

