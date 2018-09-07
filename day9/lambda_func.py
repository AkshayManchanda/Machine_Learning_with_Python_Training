'''
double = lambda x: x*2
print(double(5))

#agar usko with the help of func(def) bnaana h to:

def double(x):
    return x*2
print(double(5))

#use of lambda with filter

li=[5,7,22,97,54,62,77,23,73,61]

final_list = list(filter(lambda x:(x%2!=0),li)      #filter list ki ek ek value ko daalra h and return krra h.. if kisi variable me daalte to loop se access krna pdhta thats y list me daaldia taaki easily print hojaye
print(final_list)
'''
#agar filter use ni karna to do like this:

'''
def alter(values,check):
    return[val for val in values if check(val)] # condition for check hora h phle for every val in values if check(val) agr true h to val me jayga.. joki list bnri h

my_list=[1,2,3,4,5]
another_list = alter(my_list,lambda x: x!=5)
print(another_list)
'''
#isi ko filter ke saath:
'''
my_list=[1,2,3,4,5]
another_list = list(filter(lambda x: x!=5,my_list))    #filter ke andar phla argument is check condition
print(another_list)
'''


#TASK
#WAP remove numbers from string using lambda() or filter() method and print answer as string
'''
z=input("Enter string with numbers: ")
list12=list()
for i in range(len(z)):
    list12.append(z[i])
print(list12)
another_list = list(filter(lambda x: x not in [str(n) for n in range(10)] ,list12))
print(another_list)
str="".join(another_list)

#or can be done as:

def alter(values,check):
    return list(filter(check,values))

def remove_numbers(values):
    return alter(values,lambda x: x not in [str(n) for n in range(10)]) #since range gives int value hence we have converted into string
a=input("Enter string with numbers:- ")
print(remove_numbers(a))
a=remove_numbers(a)
str1 = "".join(a)
print(str1)
'''
#TASK
#WAP to remove particular letter from string using lambda and filter function and print as string
'''
z=input("Enter string with numbers: ")
list12=list()
for i in range(len(z)):
    list12.append(z[i])
print(list12)
n=input("Enter a character to be removed: ")
another_list=list(filter(lambda x: x not in n,list12))    #or x!=n
print(another_list)
str=''.join(another_list)
print(str)
'''

#USE OF LAMBDA() WITH MAP()
'''
li=[5,7,22,97,54,62,77,23,73,61]

final_list = list(map(lambda x: x*2,li))
print(final_list)
'''

#USE OF REDUCE() WITH LAMBDA()

'''
from functools import reduce        #IMPORT

li=[5,8,10,20,50,100]

sum = reduce((lambda x,y: x+y),li)    #x to li se aara h but y zero lera h.. zero se add hora as default add sub me 0 se add hota h.. mul and div me 1 se(as sum=0 and sum=1 lete h hum)

print(sum)
'''
#SOME OTHER BUILT IN FUNCTIONS

class Currency:
    def __init__(self,code, exchange_to_usd):
        self.amount = 0.00
        self.code=code
        self.exchage_to_usd = exchange_to_usd
    
    def set_amount(self,amount):
        self.amount = amount
    
    def in_currency(self,amount):
        return amount/self.exchange_to_usd
    
    def to_usd(self,amount=None):
        to_convert = amount or self.amount
        return to_convert * self.exchange_to_usd
    
    def __eq__(self,other):
        # Exactly equal ==
        return self.to_usd() == other.to_usd()
    
    def __gt__(self,other):
        # Greater than >
        return self.to_usd() > other.to_usd()
    
    def __lt__(self, other):
        # Less than <
        pass
    
    def __le__(self,other):
        # Less than or equal to <=
        pass
    
    def __ge__(self,other):
        # Greater than or equal to >=
        pass
    
pounds = Currency("GBP",1.21)   #look from internet
pounds.set_amount(1000)         
euros = Currency("EUR",1.07)    #look from internet
euros.set_amount(1000)

print(pounds > euros)

