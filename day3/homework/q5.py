list=[]
print("Enter the marks for each subject(OUT OF 100):- ")
for i in range(5):
    print("Enter marks for ",i+1," subject: ")
    m=float(input())
    list.append(m)
sum=float(0)
for i in list:
    sum+=i
sum/=len(list)
if(sum>80):
    print("grade: A")
elif(sum<=80 and sum>60):
    print("grade: B")
elif(sum<=60 and sum>30):
    print("grade: C")
else:
    print("grade: D")    
    



