'''
class MyClass:
    variable = "blah"
    def function(self):    #without self cannot define a function.. it is similar to this in C++
        #a=10
        print("This is a message inside the class.")
        #return a
myobjectx = MyClass()          #creating object/instance
print(myobjectx.variable)
print(myobjectx.function())     #output me none aara h coz nothing is returned
myobjectx.function()            #aisa kra to none print ni krega    
'''
'''
class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.real = r
        self.imag = i
        
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))
        

a=ComplexNumber()
a.getData()

a=ComplexNumber(3,5)
a.getData()
'''
'''
#ques
class Vehicle:
    def __init__(self,d="",c=0.0,n=""):
        self.desc=d
        self.cost=c
        self.name=n
    def getData(self):
        print("{} is a {} worth ${}".format(self.name,self.desc,self.cost))
car1=Vehicle("red convertible", 60000.0,"Fer")
car2=Vehicle("blue van",10000.0,"Jump")
car1.getData()
car2.getData()
'''
'''
class Emp:
    empCount=0
    def __init__(self,n="",s=0):
        self.name=n
        self.sal=s
        Emp.empCount+=1         #classnanme.varible
    def getData(self):
        print("Name is: {} , Salary is: {}".format(self.name,self.sal))
        
emp1 = Emp("zara",2000)
emp1.getData()
print("Total Employee : ", Emp.empCount)
emp2 = Emp("nishant",67000)
emp2.getData()
print("Total Employee : ", Emp.empCount)
'''
'''
class Vehicles:
    def general_usage(self):
        print("genreal use: transportation")
class Car(Vehicles):
    def __init__(self):
        print("I'm car")
        self.wheel=4
        self.has_roof=True
    def specific_usage(self):
        self.general_usage()           #base class method
        print("specific usage: commute to work, vacation with family")
class MotorCycle(Vehicles):
    def __init__(self):
        print("I'm motor cycle")
        self.wheel = 2
        self.has_roof = False
    def specific_usage(self):
        self.general_usage()            #base class method
        print("Specific use: road trip, racing")
c=Car()
c.specific_usage()

m = MotorCycle()
m.specific_usage()
print(isinstance(c,Car))            #true
print(isinstance(c,MotorCycle))     #false
print(isinstance(c,Vehicles))       #true
print(isinstance(m,Car))            #false
print(isinstance(m,MotorCycle))     #true
print(isinstance(m,Vehicles))       #true        #as class ko check krra h ki class subclass h right wali class ki

print(issubclass(Car,Vehicles))     #true
print(issubclass(Vehicles,Car))     #false
'''
'''
#multiple inheritance
class Father:
    def gardening(self):
        print("i enjoy gardening")
class Mother:
    def cooking(self):
        print("i love cooking")
class Child(Father,Mother):
    def skills(self):
        print("i enjoy sports")
        #self.gardening()
        #self.cooking()                #aise bhi kar sakte the if ek hi seteeno print kraane hai

c = Child()
c.gardening()
c.cooking()
c.skills()
'''
'''
class Father:
    def skills(self):
        print("i enjoy gardening")
class Mother:
    def skills(self):
        print("i love cooking")
class Child(Father,Mother):
    def skills(self):
        print("i enjoy sports")
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.skills()          #THIS WILL CALL CHILD CLASS SKILL METHOD
'''
'''
class Human:
    def __init__(self,n='',g='',o='',m='',w=''):
        self.name=n
        self.gender=g
        self.occ=o
        self.mess=m
        self.work=w
    def speaks(self):
        print(mess)
    def getData(self):
        print("name: {}, gender: {}, occupation: {}".format(self.name,self.gender,self.occ))
a=Human("Tom Cruise",'Male','Actor',"I am Ethan Hunt of Mission impossible","Shoot movie")
b=Human("Maria Sharapova","Female","Tennis Player","i won 5 grand slams","play tennis")
a.getData()
b.getData()
'''

class Person:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last
    def __str__(self):                # if we want to print string then use this
        return self.firstname + " " + self.lastname
class Employee(Person):
    def __init__(self,first,last,staffnum):
        super().__init__(first,last)        #for calling constructor of the superclass
        self.staffnumber=staffnum

x=Person("Narge", "Simpson")
y=Employee("Homer","Simpson","1007")

print(x)
print(y)

#===hw===
#similar try for mother and father and update by child class 

    