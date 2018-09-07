num=int(input("Enter a number: "))
sum=0
for i in range(1,num+1):
    sum=0
    for j in range(1,i+1):
        print(j,end='')
        if(j==i):
            print("=",end='')
        else:
            print("+",end='')
        sum=sum+j
    print(sum)