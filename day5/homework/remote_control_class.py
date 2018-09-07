a=['a','b','c','d','e','f'] 
class RemoteControl:
       def control(self,b):
           try:   
               choice='y'
               while(True):
                   print("press 'y' to change channel to next or 'n' to quit: ")
                   choice=input()
                   if(choice=='y' or choice=='Y'):
                       print(next(b))
                   elif choice=='n' or choice=='N':
                       print("TV IS SWITCHED OFF..")
                       break
                   else:
                        print("Wrong choice.. Enter again: ")
           except StopIteration as s:
                print("List is over.. Starting again!")
                b=iter(a)
                self.control(b)       
print("TV IS SWITCHED ON..  ")
b=iter(a)
print(next(b))              
user=RemoteControl()               
user.control(b)  
            