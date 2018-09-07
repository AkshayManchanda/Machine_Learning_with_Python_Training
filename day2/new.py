'''a=10
b=20
list=[10,20,30,40,50]
if(a in list):                          can be written as if a in list             #membership operator
    print('a is in given list')
else:
    print('a is not in given list')
if(b not in list):                      #membership operator
    print('b is not given in list') 
else:
    print('b is in given list')


a=20
b=20
if(a is b):                             #identity operator
    print('a,b have same identity')
else:
    print('a,b are different')
b=10
if(a is not b):                         #identity operator
    print('a,b have different identity')
else:
    print('a,b have same identity')


#input
a=input('Enter your no:-')
print(a)
print(type(a))
b=a*2
print(b)
a=int(a)                        #converting #similarly float     
print(a)
print(a*2)                      #will multiply
print(type(a))


print('this is print function')         #type 1
a=3
print('the value of a is:-',a)          #type 2
print('enter value','of a:-', sep='@',end='')   #type 3
a=input()
print(a)

a,b,c=10,20,30
print('the value of a is {} and b is {}'.format(a,b))  #type 4
'''

 

