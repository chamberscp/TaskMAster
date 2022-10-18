# Import modules
# Breakout of functions
    # Login/ Greeting
    # Display tasks
    # Add Tasks
    # Remove Tasks
    # Show whole list
    # Count remaining tasks in list
    # Exit
    
import sys
import datetime
from pyfiglet import Figlet
import sqlite3

con = sqlite3.connect("taskmasterdb.db")

f = Figlet(font='big')
print(f.renderText('Task Master 3000'))

print("Please enter your username: ")

userlist = ["elliot", "chris"]
name = input()

if name.lower() in userlist:
    print(f'Welcome ' + name )
else:
    print("User not authorized.  Please enter valid username: ")


def greet(name):
   pass
    

def displaytop5(tasks):
    pass
   
def addtask():
    pass

def deltask():
    pass

def counttasks():
    pass

def exitmsg():
    pass