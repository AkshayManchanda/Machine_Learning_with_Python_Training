'''
import os               #import package operating system
import time
curDir=os.getcwd()      #get current working directory
print(curDir)
os.mkdir('newDir')      #create new directory
time.sleep(2)               #execute neeche ka after 2 seconds(hold for 2 sec)
os.rename('newDir','newDir2') #rename dir
time.sleep(2)
os.rmdir('newdir2')
'''
'''
import datetime
print(datetime.datetime.now())  #print current date and time
'''
'''
#upar wale ko short me likhna
from datetime import *
print(datetime.now())  #print current date and time
'''