a=0
b=1
n=input("enter the number of terms: ")
n=int(n)
print(a,"  ",end='')
print(b,"  ",end='')
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(b,"  ",end='')
