
'''
#shuffle list
from random import *
a=[1,2,3,4,5]
print('old list:- ',a)
for i in range(5):
    shuffle(a)
    print('new list:- ',a)
'''

'''
#function
def printme(str):
    print(str)
    
printme('hello123')
'''

'''
def changeme(mylist):
    mylist.append([1,2,3,4]);               #function in list to add at end as it is mutable ..(list ke andar list matlab nested list)
    print("values inside the function: ",mylist)
    return            #returns nothing
mylist=[10,20,30]
changeme(mylist)
print("values outside the function: ",mylist)       #andar bahr dono me same(pass by reference as wo variable pass karre the)
'''

'''
def changeme(mylist):
    mylist=[1,2,3,4]
    print('values inside the function: ',mylist )
mylist=[10,20,30]
changeme(mylist)
print("values outside the function: ",mylist)               #call by value as andar us variable ko local bna dia to wo sirf usi function ke lie available h.. to bahr chng nj hoga kch
'''
'''
def area(l,b):
    area1=0.5*l*b
    print('area is: ',area1)
    return area1
    
a=area(2,3)
print(a)
'''
'''
def area(l,b):
    area1=0.5*l*b
    area2=l*b
    print('area is: ',area1)
    return (area1,area2)        #return tuple
    
a=area(2,3)
print(a)
'''
'''
def area(l,b):
    area1=0.5*l*b
    area2=l*b
    print('area is: ',area1)
    return area1,area2        #still return tuple
    
a=area(2,3)
print(a)
'''
'''
def area(l,b):
    area1=0.5*l*b
    area2=l*b
    print('area is: ',area1)
    
a=area(2,3)
print(a)        #as returned nothing
'''
'''
def area(l,b):
    print("l: ",l)
    print("b: ",b)
    area1=0.5*l*b
    area2=l*b
    print('area is: ',area1)
    return area1,area2        #still return tuple
    
a=area(b=3,l=2)  #keyword argument
print(a)
'''


