# Import modules
# Breakout of functions
    # Login/ Greeting
    # Display tasks
    # Add Tasks
    # Remove Tasks
    # Show whole list
    # Count remaining tasks in list
    # Exit
    
from curses.ascii import isalpha
import sys
import datetime
from pyfiglet import Figlet
import sqlite3

con = sqlite3.connect("taskmasterdb.db")

f = Figlet(font='big')
print(f.renderText('Task Master 3000'))

count = 0

while count < 3:
    count = 0
    user_list = ["Elliot", "Chris"]
    user_name = input("Please enter your username: ")
    if user_name in user_list:
        print(f"Welcome " + user_name)
        break
    else:
        print("Unauthorized user.  Please enter valid username: ")                            
                    

def addtask():
    pass

def displaytop5(tasks):
    pass
   

def deltask():
    pass

def counttasks():
    pass

def exitmsg():
    pass