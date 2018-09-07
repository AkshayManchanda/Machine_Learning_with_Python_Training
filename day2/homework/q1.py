a=input('Enter first operand: ')
b=input('Enter second operand: ')
a=float(a)
b=float(b)
c=input('Enter the operator(+,-,*,/): ')
if(c == '+'):
    print(a,c,b,sep=' ',end=' ')
    print(" = ", a+b)
elif(c == '-'):
    print(a,c,b,sep=' ',end=' ')
    print(" = ", a-b)
elif(c == '*'):
    print(a,c,b,sep=' ',end=' ')
    print(" = ", a*b)
elif(c == '/'):
    print(a,c,b,sep=' ',end=' ')
    print(" = ", a/b)
else:
    print('WRONG OPERATOR ENTERED!!')

    