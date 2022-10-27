# https://github.com/chamberscp/TaskMaster

import datetime
import os
import sys
import time
from   pyfiglet import Figlet
from   rich     import print as rprint


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
    break
else:
    print("Unauthorized user.  Please enter valid username: ")
    quit()            
                    
# Function to add tasks
def add(newtask):
  
    f = open(user_name +'.txt', 'a')
    f.write(newtask)
    f.write("\n")
    f.close()
    newtask = '"'+newtask+'"'
    rprint(f"Added the task: {newtask}. Getting your new list. Please wait....") 
    time.sleep(2)
    show()
   
 # Function to Mark Tasks Complete
def complete(num):
    try:
        update()
        num = int(num)
        f = open(user_name + '.txt', 'a')
        st = '***COMPLETED*** '+str(datetime.datetime.today()).split()[0]+' '+d[num]
        f.write(st)
        f.write("\n")
        f.close()
        rprint(f"Marked task #{num} as complete. Getting your new list. Please wait....")
        time.sleep(2)
        
        with open(user_name +'.txt', 'r+') as f:
            lines = f.readlines()
            f.seek(0)
			
            for i in lines:
                if i.strip('\n') != d[num]:
                    f.write(i)
            f.truncate()
        show()
    
    except:
        print(f"There is no task #{num}.")
  
# Function to delete a task
def delete(number):
    try:
        number = int(number)
        update()
        with open(user_name +'.txt', "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip('\n') != d[number]:
                    f.write(i)
            f.truncate()
        rprint(f"Deleted task #{number}")
    except Exception as e:
        rprint(f"There is no task #{number}.")
        show()
        
 # Function that shows a list of tasks
def show():
    with open(user_name + '.txt', 'r') as q:
        if os.path.getsize(user_name +'.txt') <1:
            print("You don't have any tasks")
        else:
            enum()
            '''data = q.read().splitlines()
            total_lines=len(data)
            first_line=0
            skipped_lines=15
            print("\n".join(data[first_line:skipped_lines]))
            while skipped_lines <= total_lines:
                print("\n".join(data[first_line:skipped_lines]))
                first_line = skipped_lines
                skipped_lines = skipped_lines + 15
                myinput=input("Press ENTER key to continue or press q to quit")
                if myinput.lower() == 'q':
                    break
                else:
                    print("\n".join(data[first_line:skipped_lines]))'''
            
def enum():
    with open(user_name+'.txt') as f:
        for index, line in enumerate(f,start=1):
            print('{}. {}'.format(index, line.strip()))
                
# Function to update list of tasks
def update():
    try:
        f = open(user_name +'.txt', 'r')
        c = 1
        for line in f:
            line = line.strip('\n')
            d.update({c: line})
            c = c+1
    except:
        print("You have no pending tasks")

def count():
    with open(user_name + '.txt', "r") as anothervar:
        var1 = len(anothervar.readlines())
        if var1 < 1:
            print("You have 0 tasks left")
        else:
            rprint(f"You have {var1} tasks left")
            time.sleep(2)
            show()  
                  
        
# Main block
if __name__ == '__main__':
    try:
        d = {}
        don = {}
        args = sys.argv
        
        if(args[1] == 'delete'):
            args[1] = 'delete'
        
        if(args[1] == 'add' and len(args[2:]) == 0):
            print("You forgot to list the task after the add command")
            
        elif(args[1] == 'done' and len(args[2:]) ==0):
            print("You forgot to tell me what number to mark as complete.  Please try again")
        
        elif(args[1] == 'delete' and len(args[2:]) == 0):
            print("You forgot to tell me what number to delete.  Please try again")
        
        else:
            globals()[args[1]](*args[2:])
    finally:
            update()
        
        
        
        