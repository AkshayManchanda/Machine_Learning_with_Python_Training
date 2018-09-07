a=int(input("Enter 1st side of triangle: "))
b=int(input("Enter 2nd side of triangle: "))
c=int(input("Enter 3rd side of triangle: "))
if((a+b)>c and (b+c)>a and (a+c)>b):
    s=(a+b+c)/2
    print("Area of triangle is: ",(s*(s-a)*(s-b)*(s-c))**0.5)
    