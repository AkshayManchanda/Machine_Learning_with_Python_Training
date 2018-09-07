num=int(input("Enter a number to be reversed: "))
print("The number in reversed order is: ")
for i in range(len(str(num))):
    m=num%10
    print(m,end='')
    num//=10