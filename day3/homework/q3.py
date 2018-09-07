l_range=int(input("Enter the lower range: "))
u_range=int(input("Enter the upper range: "))
d=int(input("Enter the number for which divisibility should be checked: "))

for i in range(l_range,u_range,1):
    if(i%d==0):
        print(i)
