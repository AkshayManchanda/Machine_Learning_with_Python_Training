num=int(input("Enter a number: "))
for i in range(num):
    
    for j in range(num):
        if(i!=j):
            print('0 ',end='')
        else:
            print('1 ',end='')
    print('')