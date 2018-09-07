a='akshay manchanda'
print("capitalize() : ",a.capitalize())

print("upper() : ",a.upper())

b="  aKshaY  "
print("swapcase() : ",b.swapcase())

print("strip() : ",b.strip())

print("replace()",b.replace('a','b'))   #sab a ko replace with b
print("replace()",b.replace('a','b',1)) #pehla hi hua h kyuki max is 1 to replace

c='sadds12'
print("isalnum() : ",c.isalnum())

str=''
seq=['a','b','c']
b=str.join(seq)     #jo jo phle h individual unko string se join kraana chahte ho to(khaali h to khaali se join ho jaygi)
print(b)

str='@'
seq=['a','b','c']
b=str.join(seq)     #@ se join hogi
print(b)

d='123212'
print("isdigit() : ",d.isdigit())

print("isnumeric() : ",d.isnumeric())
