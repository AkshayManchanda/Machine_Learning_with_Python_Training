num=int(input("Enter a number: "))
sum=0
for i in range(len(str(num))):
    sum=sum+(num%10)
    num=num//10
print("The sum of the digits in the number entered is: ",sum)