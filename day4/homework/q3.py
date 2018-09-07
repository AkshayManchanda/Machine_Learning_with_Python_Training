def calc(choice):
    if(choice!=1 and choice!=2 and choice!=3 and choice!=4):
        print("Wrong choice!!")
        return
    a=int(input("Enter 1st num: "))
    b=int(input("Enter 2nd num: "))
    if choice==1:
        c=a+b
        o='+'
    elif choice==2:
        c=a-b
        o='-'
    elif choice==3:
        c=a*b
        o='*'
    elif choice==4:
        c=a/b
        o='/'
    print("{} {} {} = {}".format(a,o,b,c))
print("Select operation.\n1. Add\n2.Subtract\n3.Multiply\n4.Divide")
ch=int(input("Enter choice (1/2/3/4): "))
calc(ch)