# https://github.com/chamberscp/TaskMaster

import sys
import  os
import datetime
import time
from pyfiglet import Figlet

#Figletdisplays the taskmaster MASTER 3000 Logo in "big" wordart format
f = Figlet(font='big')
print(f.renderText('Task Master 3000'))

# Commands Section - Defines the commands the user can input.
x = """              Task Master 3000 Commands:
./taskmaster add "task name"  		# Adds new tasks
./taskmaster show               	# Show all remaining tasks
./taskmaster complete NUMBER        # Marks a task as complete. If it is the first task, it will be deleted.
./taskmaster delete NUMBER          # Delete a task
./taskmaster count                  # Counts the number of remaining tasks
"""
print(x)

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
    #add enumerate here????
    f = open(user_name +'.txt', 'a')
    f.write(newtask)
    f.write("\n")
    f.close()
    newtask = '"'+newtask+'"'
    print(f"Added the task: {newtask}") 
    show()
   
 # Function to Complete a todo
def complete(num):
    try:
        update()
        num = int(num)
        f = open(user_name + '.txt', 'a')
        st = 'x '+str(datetime.datetime.today()).split()[0]+' '+d[num]
        f.write(st)
        f.write("\n")
        f.close()
        print(f"Marked task #{num} as complete. Getting your new list. Please wait....")
        time.sleep(3)
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
  
# Function that deletes a task
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
        print(f"Deleted task #{number}")
    except Exception as e:
        print(f"There is no task #{number}.")
        show()
        
 # Function that shows a list of tasks
def show():
    with open(user_name + '.txt', 'r') as q:
        if os.path.getsize(user_name +'.txt') <1:
            print("You don't have any tasks")
        else:    
        #   for i, line in enumerate(q, start=1):
        #        pass
            data = q.read().splitlines()
            total_lines=len(data)
            first_line=0
            skipped_lines=15
            while skipped_lines <= total_lines:
                print("\n".join(data[first_line:skipped_lines]))
                first_line = skipped_lines
                skipped_lines = skipped_lines + 15
                myinput=input("Press ENTER key to continue or press q to quit")
                if myinput.lower() == 'q':
                    break
                else:
                    continue
            else:
                print("\n".join(data[first_line:skipped_lines]))
        
                
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
    with open(user_name + '.txt', "r") as lc:
        var1 = len(lc.readlines())
        if var1 < 1:
            print("You have 0 tasks left")
        else:
            print(f"You have {var1} tasks left")        
        
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
        
        
        
        