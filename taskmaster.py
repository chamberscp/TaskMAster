# Import modules
# Breakout of functions
    # Login/ Greeting
    # Help Section/ Commands
    # Display tasks
    # Add Tasks
    # Remove Tasks
    # Show whole list
    # Count remaining tasks in list
    # Exit
    

import sys
from pyfiglet import Figlet
import datetime

#Figletdisplays the TASK MASTER 3000 Logo in "big" wordart format
f = Figlet(font='big')
print(f.renderText('Task Master 3000'))

count = 0
#Login Section.  Requires the user to login (case sensative).  User will have 3 attempts to login before being booted.
while count < 3:
    count = 0
    user_list = ["Elliot", "Chris"]
    user_name = input("Please enter your username: ")
    if user_name in user_list:
        print(f"Welcome " + user_name)
        break
    else:
        print("Unauthorized user.  Please enter valid username: ")                            
                    
# Commands Section - Defines the commands the user can input.

def commands():
    avcmds = """Commands 
    ./task add "task name"      - Adds a new task
    ./task delete NUMBER        - Deletes a task
    ./task show                 - Shows all remaining tasks and provides a count of remaining tasks
    ./task commands             - Shows this Commands Section"""
    sys.stdout.buffer.write(avcmds.encode('utf8'))
    
# Quick display of the top five tasks in the order they were input (via timestamp)
def displaytop5(tasks):
    pass   


 