import os 
import sys
def clear():os.system('CLS')
wrong=0
while True:
    
    clear()
    password = input("enter password:")

    if password=="123":
        
        break
    elif wrong == 2:
        sys.exit()
    else:
        wrong = wrong+1
        print("error")
        
        
    

os.system(r"explorer.exe D:\programing_videos")
