num=int(input("Enter a number: "))
on=num
nn=0
for i in range(len(str(num))):
    m=num%10
    num//=10
    nn=nn*10+m
if(on==nn):
    print("it is palindrome!")
else:
    print("It is not a palindrome!")