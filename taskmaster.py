# https://github.com/chamberscp/TaskMaster

import datetime
import fileinput
import os
import re
import sys
import time
from   pyfiglet import Figlet
#from   rich     import print as rprint
#from   rich.pretty    import pprint

allTasks = []       
PAGE_LENGTH = 15    
page = 0

COMPLETED = 0
DESCRIPTION = 1

#Figletdisplays the taskmaster MASTER 3000 Logo in "big" wordart format
f = Figlet(font='big')
print(f.renderText('Task Master 3000'))

# Commands Section - Defines the commands the user can input.
menu = """              Task Master 3000 Commands:
./taskmaster add "task name"  		# Adds new tasks
./taskmaster show               	# Show all remaining tasks
./taskmaster complete NUMBER            # Marks a task as complete. If it is the first task, it will be deleted.
./taskmaster delete NUMBER              # Delete a task
./taskmaster count                      # Counts the number of remaining tasks
"""
print(menu)

#Login Section.  Requires the user to login (case sensative). 
user_list = ["Elliot", "Chris"]
user_name = input("Please enter your username: ")
while user_name in user_list:
    print(f"Welcome " + user_name)
    time.sleep(1.5)
    break
else:
    print("Unauthorized user.  Please enter valid username: ")
    quit()            
                    
# Function to add tasks
def add(newtask):
    with open(user_name +'.txt', "r+") as f:
        f.readlines()
        f.write("\n")
        f.write(f'{[True]}, {[newtask]}')
        print(f"Added the task: {newtask}. Getting your new list. Please wait....") 
        time.sleep(2)
        show()
   
 # Function to Mark Tasks Complete (credit to argiopetech@github for completion function)
#def complete(num):
def completeTask(num):
    toComplete = {num}(1, len(allTasks))
    
    allTasks[COMPLETED] = True
 
 # Function to delete all tasks that exist before first incomplete tasks(credit to argiopetech@github for completion function)   
def del_top_cmplt_tasks():
    while allTasks[0][COMPLETED]:
        del allTasks[0]    

# Function to delete a task
def delete(num):
    try:
        num = int(num)
        with open(user_name +'.txt', "r+") as f:
            lines = f.readlines()
            f.seek(0)
            f.truncate()
            for i, line in enumerate(lines):
                if i not in {3-1}:
                    f.write(line)
                
            print(f"Deleted task #{num}.  Getting your new list.")
            time.sleep(2)

        show()    
    except Exception as e:
        print(f"There is no task #{num}. Getting your task list")
        time.sleep(2)
        show()    
    
# Function that shows a list of tasks
def show():
    with open(user_name + '.txt', 'r+') as q:
        if os.path.getsize(user_name +'.txt') <1:
            print("You don't have any tasks")
        
        else:
            #del_top_cmplt_tasks()
            allTasks =q.read().split('\n')
            currentPos = 0
            stepPos = 15
            
            for i in range(0, len(allTasks)):
                if currentPos < stepPos:
                   currentPos += 1
                   print(f'{i+1}. {allTasks[i]}')                  

                else:            
                    currentPos += 1
                    blah = input("Press any key to continue")
                    print(f'{i+1}. {allTasks[i]}')                
                    stepPos += 15
                    
# Function to count the remaining tasks
def count():
    with open(user_name + '.txt', "r") as anothervar:
        var1 = len(anothervar.readlines())
        if var1 < 1:
            print("You have 0 tasks left")
        else:
            print(f"You have {var1} tasks left")
            time.sleep(2)
            show()  
                     
# Main block
if __name__ == '__main__':
    try:
      
        args = sys.argv
        
        if(args[1] == 'delete'):
            args[1] = 'delete'
        
        if(args[1] == 'add' and len(args[2:]) == 0):
            print("You forgot to list the task after the add command")
            
        elif(args[1] == 'complete' and len(args[2:]) ==0):
            print("You forgot to tell me what number to mark as complete.  Please try again")
        
        elif(args[1] == 'delete' and len(args[2:]) == 0):
            print("You forgot to tell me what number to delete.  Please try again")
            
        else:
            globals()[args[1]](*args[2:])
    finally:
            pass 