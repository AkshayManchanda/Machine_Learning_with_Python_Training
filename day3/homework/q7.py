a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
list=[]
list.append(a)
list.append(b)
list.append(c)
for i in range(3):
    for j in range(3):
        for k in range(3):
            if(i!=j and j!=k and k!=i):
                print(list[i],list[j],list[k],sep=' ')