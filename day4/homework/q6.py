'''
'a=int(input("Enter a number in decimal: "))
print("binary: ",bin(a))
print("octal: ",oct(a))
print("hexadecimal: ",hex(a))
'''
#or
'''
def d2b(a):
    l=[]
    c=a
    while(c>0):
        b=c%2
        l.append(b)
        c=c//2
    for i in l[::-1]:
        print(i," ")
l=d2b(16)
'''
'''
def d2o(a):
    l=[]
    c=a
    while(c>0):
        b=c%8
        l.append(b)
        c=c//8
    for i in l[::-1]:
        print(i," ")
l=d2o(16)
'''






















def d2b(a):
    b=a
    l=[]
    while(a>0):
        c=a%2
        b=a//2
        l.append(c)
    print(l)
d2b(16)