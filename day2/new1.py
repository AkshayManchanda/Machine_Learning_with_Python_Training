'''import math #as m also can be written

a=math.pi   #a=m.pi
print(a)
'''

'''
from math import pi        #import only pi from math
b=2*pi
print(b)
'''

'''
from math import *   #import everything from math
b=2*pi
print(b)
'''
'''
food = 'spam'
if food == 'spam':
    print('Ummmm, my favourite!')
print('I feel like saying it 100 times...')
print(100*(food+'!'))    
'''

'''
food = 'spam'
if food == 'spam':
    print('Ummmm, my favourite!')
else:
    print('No!')
'''
'''
import random
a=random.randint(0,45)
str=''
if(a>43):
    str='larger'
elif(a>35 and a<=43):
    str = 'medium'
elif(a>25 and a<=35):
    str='small'
else:
    str='not eligible'
    
print('the value is {} and is {}'.format(a,str))
'''

'''
#for loop

for friend in ['Margot','Kathryn','Prisila']:
    invitation = "Hi " + friend + ". Please come to my party on Saturday!"
    print(invitation)
'''

'''
name = 'harrison'
guess = input("So I'm thinking of person's name. Try to guess it: ")
pos = 0
while guess!=name and pos<len(name):
    print("Nope, that's not it! Hint: letter ",end='')
    print(pos+1,'is',name[pos]+".",end='')
    guess = input("Guess again: ")
    pos = pos + 1
if pos==len(name) and name!=guess:
    print("Too bad, you couldn't get it. The name was", name + ".")
else:
    print("\nGreat, you got it in ",pos + 1,"guesses!")
'''
'''
for i in [12,16,17,24,29,30]:
    if i%2 ==1: #if number is odd
        pass                                        #will do nothing
        print('this is pass block') 
    print(i)
print('done')
'''


    


