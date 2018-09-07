from task_area_funcs import *

def area():
    print("choose to calculate area: ",end="\n")
    print("1. triangle",end='\n')
    print("2. circle",end='\n')
    choice=int(input("enter choice: "))
    if(choice==1):
        t_area()
    elif(choice==2):
        c_area()
    else:
        print("WRONG CHOICE!!")
area()