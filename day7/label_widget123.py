'''
from tkinter import *

root = Tk()     #creates a blank window
theLabel = Label(root,text="This is too easy")
theLabel.pack() #basically places this widget inside the window
root.mainloop() #keeps the window open, the close button breaks the loop
'''
'''
from tkinter import *

root = Tk()
#frame is a rectangular area that contains other buttons
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)           #frame divides window in frame
bottomFrame.pack(side=BOTTOM)       #by default pack hamesha top pe place krta h.. if khi or to define

button1 = Button(topFrame,text="Button 1",fg='red')     #fg is foregroung color.. or text color.. we can also use hex code
button2 = Button(topFrame,text="Button 2",fg='blue')
button3 = Button(topFrame,text="Button 3",fg='green')
button4 = Button(bottomFrame,text="Button 4",fg='purple')

#these buttons will be on top
button1.pack(side=LEFT) #places as far left as possible
button2.pack(side=LEFT)
button3.pack(side=LEFT)
#button4 is on the Bottom
button4.pack(side=BOTTOM)
root.mainloop()
'''
'''
from tkinter import *

root = Tk()

one = Label(root,text="one",bg='red',fg='white')    #bg is background color
one.pack()
two = Label(root,text='two',bg='green',fg='black')  
two.pack(fill=X)    #fill=X-> makes the widget as wide as the parent
three = Label(root,text='three',bg='blue',fg='white')
three.pack(side=LEFT,fill=Y)

root.mainloop()
'''
'''
from tkinter import *

root = Tk()

label_1 = Label(root,text="Name")
label_2 = Label(root,text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

#widgets centered by default, sticky option to change
label_1.grid(row=0,sticky=E)    #E is east.. similarly W, N, S. ... if center me to N+S+E+W (grid ke andar kaise align krna h left align right align so on
label_2.grid(row=1,sticky=E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

#widgets can take up more than one cell with columnspan and rowspan
c = Checkbutton(root,text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()
'''
# to quit button use root.quit in command

#ques make name = akshay pass = manchanda then when click on keep me logged in label daalana h ki logged in
#ans->
'''
from tkinter import *

root = Tk()

def func():
    if(e1_value.get=="akshay" and e2_value.get()=='manchanda'):
        print("logged in")

e1_value=StringVar()
e2_value=StringVar()

label_1 = Label(root,text="Name")
label_2 = Label(root,text="Password")
entry_1 = Entry(root,textvariable=e1_value)
entry_2 = Entry(root,textvariable=e2_value)

#widgets centered by default, sticky option to change
label_1.grid(row=0,sticky=E)    #E is east.. similarly W, N, S. ... if center me to N+S+E+W (grid ke andar kaise align krna h left align right align so on
label_2.grid(row=1,sticky=E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

#widgets can take up more than one cell with columnspan and rowspan
c = Checkbutton(root,text="Keep me logged in",command=func)
c.grid(columnspan=2)
root.mainloop()
'''
'''
from tkinter import *

root = Tk()

def leftClick(event):
    print("Left")

def middleClick(event):
    print("Middle")

def rightClick(event):
    print("Right")
    
frame = Frame(root, width=300, height=200)
#event is something the user does to the widget, function that gets called
frame.bind("<Button-1>",leftClick)       #button 1 is predefined .. it calls leftClick function    #bind function links to function when event occurs
frame.bind("<Button-2>",middleClick)     #button 2 is predefined .. it calls middleClick function
frame.bind("<Button-3>",rightClick)      #button 3 is predefined .. it calls rightClick function
frame.pack()

root.mainloop()
'''

#ques
#do button banaane hai.. when right click kra print message pe  to console pe print some message.. if quit pe left click to quit

'''
from tkinter import *

root = Tk()

def rightClick(event):
    print("Right")
    
button1 = Button(root,text="Print Message",fg='black')
button1.pack(side=LEFT)
button2 = Button(root,text="quit",fg='black',command=root.quit)
button2.pack(side=LEFT)
button1.bind("<Button-3>",rightClick)

root.mainloop()
'''

'''
from tkinter import *

class BuckysButtons:
    
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
    
        self.printButton = Button(frame,text="Print Message",command=self.printMessage)
        self.printButton.pack(side=LEFT)
        
        self.quitButton = Button(frame,text="Quit",command=frame.quit)
        self.quitButton.pack(side=LEFT)
    
    def printMessage(self):
        print("Wow, this actually worked!")

root = Tk()
b=BuckysButtons(root)
root.mainloop()
'''
'''
from tkinter import *
import tkinter.messagebox       #import ni hota ye krna pdhta h

root = Tk()

tkinter.messagebox.showinfo('Window Title','Monkeys can live upto 300 years.')      #to show message 1st argument is title 2nd is message
answer = tkinter.messagebox.askquestion("Question 1",'Do you like silly faces?')    #to ask ques

if answer == 'yes':
    print('LOL')
    
root.mainloop()
'''
#to work with images in python we install package pillow
'''
import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="logo.png")       #image must be in same folder.. it must be png
w1 = tk.Label(root,image=logo).pack(side='right')   #pack bhi isi me hi krdia ek baar me
explanation = "Some text will appear here..."    #koi message or text
w2 = tk.Label(root,justify=tk.LEFT,padx=10,text=explanation).pack(side='left')    #padx is to provide padding horizontally similarly pady will provide padding vertically
root.mainloop()
'''
'''
from tkinter import *

def doNothing():
    print("ok ok i won't")

root = Tk()

menu = Menu(root)
root.config(menu=menu)  #left wala input argument hai    root ke andar congif call krre h

subMenu = Menu(menu)    #since submenu is also menu and is in "menu"
menu.add_cascade(label="File",menu=subMenu) #if menu ke andar subMenu dedia to aara hai.. agr ni likhte to aise hi rhega..
subMenu.add_command(label="New Project",command=doNothing)  #command uspe lgaate hai jaha pe kuch call ho ya kuch ho aisa chaiye to
subMenu.add_command(label="New...",command=doNothing)
subMenu.add_separator()     #adds line 
subMenu.add_command(label="Exit",command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)

root.mainloop()
'''
