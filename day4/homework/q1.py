def lcm(a,b):
    if a>b:
        min=b
    else:
        min=a
    while(1):
        if(min%a==0 and min%b==0):
            return min
            break
        min+=1
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print("lcm is: ",lcm(a,b))
    