'''
try:
    fh = open('lines.txt')     #object fh... by default read pe khulti h.. agr file hogi to yehi chlega ni ho to except pe phch jayga
    for line in fh:
        print(line.strip())     #ek ek line print kara rha hai .. specially designed for file reading
except IOError as e:            #jo error aara tha wo e me chla gya if file does not exist
    print('file does not exist....!',e)
'''
'''
def main():
    try:
        for line in readfile('lines.txt'):print(line.strip())
    except IOError as e:
        print('cannot read file:',e)
    except ValueError as e:         #value error is when you give a particular type and input is not the same
        print('Bad file name',e)

def readfile(filename):
    if filename.endswith('.txt'):       #check if file end with .txt
        fh=open(filename)
        return fh.readlines()           #this func also reads lines   
    else: raise ValueError('Filename must end with.txt')

main()
#if dono galat dedie to is case me value error raise hoga as pehle wo aara hai
'''
#google "python builtin exceptions"
'''
try:
    fh=open('lines.txt')
    a=1/0
except IOError as e:
    print("cannot read file:",e)
finally:
    print("finally block")      #no matter what execute hoga ye  block
    fh.close()
#output me error jb bhi ayga kyuki error to dega hi.. bs file close krne ke lie ya kch or execute krne ke lie use krte h finally
'''
'''
#ques        H.W        class bnaani hai
#remote control wala
try:
    a=['a','b','c','d','e','f']
    b=iter(a)
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b)) #ispe error dega isko resolve krna h exception handling se
except StopIteration as s:
    print("END")
    b=iter(a)
    print(next(b))
    #try reverse
'''
#to copy one data of one file into other
'''
def main():
    infile = open('lines.txt','r')
    outfile = open('new.txt','w')
    for line in infile:
        print(line,file=outfile,end='')     #use like this.. kis file ke andar print kra rha hai
    print("done!!")
main()
'''    
'''
def main():
    buffersize = 50000 #assume buffer size
    infile = open('bigfile.txt','r')
    outfile = open('new.txt','w')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.',end='')
        buffer=infile.read(buffersize)
        print()
    print('Done...')

main()
'''
#===HW
#text file me 10 log ke naam h
#prog bnaana h jisme list hogi 5 logo ki.. 
#ab file bnaani h jisme wo list ke 5 log na ho baaki ho
'''
def main():
    buffersize = 50000 #assume buffer size
    infile = open('olives.jpg','rb') #rb and wb
    outfile = open('new.jpg','wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.',end='')
        buffer=infile.read(buffersize)
        print()
    print('Done...')
    
if __name__== "__main__" : main()       ### aagey btayga ye
'''
'''
#tkinter
import tkinter
top = tkinter.Tk()  #code to add widgets will go here...
top.mainloop()
'''
'''
from tkinter import *
window=Tk()
b1=Button(window,text='Calculate')
b1.pack()   #bs button daal deta h agr kuch ni btaya to center pe dal deta h
e1=Entry(window)
e1.pack()
window.mainloop()
'''
'''
from tkinter import *
window=Tk()

b1=Button(window,text='Calculate')
b1.grid(row=0,column=0)             #grid bnaane ke lie
e1=Entry(window)
e1.grid(row=0,column=1)
t1=Text(window,height=1,width=20)    #agr height and width ni di to bht bda aa jayga
t1.grid(row=0,column=2)
window.mainloop()
'''
'''
from tkinter import *
window=Tk()
def km_to_mile():
    print(e1_value.get())               #to print on console
    miles=float(e1_value.get())*6.2     #check for value
    t1.insert(END,miles)        
b1=Button(window,text='Calculate',command=km_to_mile)   #command matlab jb press ho to ye func pe jayga
#b1.pack()
b1.grid(row=0,column=0) 

e1_value=StringVar()        # to define that input string var honi chahiye

e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)
t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)
window.mainloop()
'''