'''
import re

# CAN YOU IDENTIFY THE PATTERN TO GET THE NAME AND AGE


NameAge = '''
#Janice is 22 and Theon is 33
#Gabriel is 44 and Joey is 21
'''

#First letter of all the names is an uppercase letter and age is represented by numbers

ages = re.findall(r'\d{1,3}',NameAge)       #1 is minimum number of digits,3 is max no of digits    #findall is a func that finds all
names = re.findall(r'[A-Z][a-z]*',NameAge)

ageDict={}
x=0

for eachname in names:
    ageDict[eachname]=ages[x]
    x+=1

print(ageDict)
'''

#Find a word in a string
'''
import re
allinform = re.findall("inform","we need to inform him with the latest information")    #first is kya find krna h 2nd is kisme?

for i in allinform:
    print(i)
'''

#get the starting and ending index of a particular string
'''
import re
Str = "we need to inform him with the latest information"

for i in re.finditer("inform",Str): #iter to iterate
    locTuple = i.span()             #span will give the starting and the end index
    #print(i)
    print(locTuple)
'''

#match letters with a particular pattern
'''
import re

Str = "Sat,hat,mat,pat"
allStr = re.findall("[shmp]at",Str) #first letter is s or h or m or p
for i in allStr:
    print(i)
'''
#or if Sat bhi krna h to
'''
import re

Str = "Sat,hat,mat,pat"
allStr = re.findall("[Shmp]at",Str)     #first letter is  S or h or m or p
for i in allStr:
    print(i)
'''

#match series of range of characters
'''
import re

Str = "Sat,hat,mat,pat"
allStr = re.findall("[h-m]at",Str) #first letter is s or h or m or p
for i in allStr:
    print(i)
'''

#replace a string
'''
import re
Food = 'hat rat mat pat'
regex = re.compile("[r]at") #to select we use re.compile() #if mat bhi chahie tha to[rm] #waise to rat likhne se bhi aajata mgr ye standard tareeka hai
Food = regex.sub("food",Food)   #sub : substitute    change krega "food" se in Food
print(Food)
'''

#match a single character    #google it


'''
import re
randStr = "12345 3459 668768 89786786l"
print("Matches:",len(re.findall("\d{5}",randStr)))    #min 5 digits wale no show krega
'''
'''
\d :- Matches any decimal digit; this is equivalent to the class [0-9].
\D :- Matches any non-digit character; this is equivalent to the class [^0-9].
\s :- Matches any whitespace character; this is equivalent to class [\t\n\r\f\v].
\S :- Matches any non-whitespace character; this is equivalent to class [^\t\n\r\f\v].
\w :- Matches any alphanumeric character; this is equivalent to class [a-zA-Z0-9_].
\W :- Matches any non-alphanumeric character; this is equivalent to class [^a-zA-Z0-9_].
'''
#removing \n from string
'''
import re

str='''
#hello i am
# nishant
# whats up!
'''
print(str)
regex = re.compile('\n')
str = regex.sub('',str)

print(str)

#\b: backspace
#\f: formfeed
#\r: carriage return
#\v: vertical tab
#\t: tab
'''
'''
import re
str2 = 'here is \\bpit'     #to print \ 
print(str2)
print(re.search(r'\\bpit',str2))
'''
#Ques: to verify the phone numbers
'''
import re
str=input("enter number (in form ###-###-####):")
#a = len(re.findall("[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]",str))
#-or-
a = len(re.findall("\d{3}-\d{3}-\d{4}$",str))
if a==1:
    print("valid")
else:
    print("invalid")
#or 
if(re.search("\d{3}-\d{3}-\d{4}$",str)):    #ending control in this
    print("its a phone number")
'''

#to validate full name
'''
import re
str=input("enter full name: ")
if re.search("\w{2,20}\s\w{2,20}",str): #\s is for space
    print("name is valid..")
else:
    print('name is not valid!!')
'''
#EMAIL VERIFICATION
'''
import re
str=input("enter email address: ")
if re.search(r"[\w.+_%-]{1,20}@[A-Za-z+-]{2,20}.[a-zA-z]{2,3}$",str):     #limit shi ni lera
    print("valid")
else:
    print("invalid")
'''