import sys
from pyfiglet import Figlet
import os.path

#Figletdisplays the taskmaster MASTER 3000 Logo in "big" wordart format
f = Figlet(font='big')
print(f.renderText('Task Master 3000'))

# Commands Section - Defines the commands the user can input.
x = """              Task Master 3000 Commands:
task add "task name"  		# Adds new tasks
task show               	# Show all remaining tasks
task delete "task number"       # Delete a task
task count                      # Counts the number of remaining tasks
"""
print(x)

#Login Section.  Requires the user to login (case sensative).  User will have 3 attempts to login before being booted.
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
    f = open('taskmaster.txt', 'a')
    f.write(newtask)
    f.write("\n")
    f.close()
    newtask = '"'+newtask+'"'
    print(f"Added the task: {newtask}") 
   
# Function that deletes a task
def delete(number):
    try:
        number = int(number)
        ud()
        with open("taskmaster.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip('\n') != d[number]:
                    f.write(i)
            f.truncate()
        print(f"Deleted task #{number}")
 
    except Exception as e:
        print(f" There is no task #{number}.")
        
 # Function that shows a list of tasks
def show():
    with open("taskmaster.txt", 'r') as q:
        if os.path.getsize('taskmaster.txt'):
            content = q.read()
            contents = content.split("\n")
            count = 0
            content in reversed(contents)
            count += 1
            print(f"{count}: {content}")
        else:
            print("You don't have any tasks")
        
# Function to update list of tasks
def ud():
    try:
        f = open('taskmaster.txt', 'r')
        c = 1
        for line in f:
            line = line.strip('\n')
            d.update({c: line})
            c = c+1
    except:
        print("You have no pending tasks")

def count():
    with open("taskmaster.txt", "r") as lc:
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
        elif(args[1] == 'delete' and len(args[2:]) == 0):
            print("You forgot to tell me what number to delete.  Please try again")
        else:
            globals()[args[1]](*args[2:])
    finally:
            ud()
        