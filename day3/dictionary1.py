d=dict(one=1,two=2,three=3)
print(d)
'''for k in d:
    print(k,d[k])
for k in sorted(d.keys()):          #isme key ki help se d[k] nikaalre h
    print(k,d[k])
for k,v in sorted(d.items()):       #k and v(value) dono ek hi baar lene h to without dictionary help
    print(k,v)
for v in  sorted(d.values()):
    print(v)
for k in d:
    print(k)
'''
'''
d['seven']=7    #insert new key
print(d)
#print(d['three1'])    #will give an error as there is no such key.. to avoid..
s=d.get('three34','key not found') #to avoid error and print message
print(s)
'''
'''
#to delete in dictionary(2 methods)
d.pop('one')    #to pop from dictionary using pop fn
print(d)
del d['two']    #using del
print(d)
'''
'''
x=dict(om=2,jai=3,**d)  #to inherit 
print(x)
'''
'''
======================================================================================================================================================================================

"HW******* user se 5 members ki name and age enter kraani h condition do logo ki same age ho.. then enter name from user then print age and also the second person with the same age "

======================================================================================================================================================================================
'''
'''
l=[1,2,3]
print('old list:- {}'.format(l))
l.append(89)    #append at end
print('new list:- {}'.format(l))
l.insert(4,99)  #if 3 ke badle 9 daaldia to bhi end me hi krdega
        #index and value upar me h
print('new list:- {}'.format(l))
#l.extend()#will do in next class
'''