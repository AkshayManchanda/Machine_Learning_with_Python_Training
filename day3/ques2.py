dic={}
for i in range(5):
    i=input("Enter name: ")
    j=input("Enter age: ")
    dic[i]=j
i=input("Enter name we will tell you the age: ")
if i in dic:
    print("age is: ",dic[i])
    for k in dic:
        if dic[k]==dic[i] and k!=i:
            print("There is another member of the family with same age whose name is ", k)
else:
    print("name not found!!")
