def gcd(a,b):
    if(a==0 and b==0):
        return 0
    if a==b:
        return a
    if a>b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print("HCF or GCD is: ",gcd(a,b))