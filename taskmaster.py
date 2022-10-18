
# Import modules
# Breakout of functions
    # Login/ Greeting
    # Help Section/ Commands
    # Display taskmasters
    # Add tasks
    # Remove tasks
    # Show whole list
    # Count remaining tasks in list
    # Exit


import sys
from pyfiglet import Figlet


#Figletdisplays the taskmaster MASTER 3000 Logo in "big" wordart format
f = Figlet(font='big')
print(f.renderText('Task Master 3000'))

count = 0

'''#Login Section.  Requires the user to login (case sensative).  User will have 3 attempts to login before being booted.
while count < 3:
    count = 0
    user_list = ["Elliot", "Chris"]
    user_name = input("Please enter your username: ")
    if user_name in user_list:
        print(f"Welcome " + user_name)
        break
    else:
        print("Unauthorized user.  Please enter valid username: ")'''                          
                    
# Commands Section - Defines the commands the user can input.
    
# Function to display top 5 tasks (from input first).  Will add a timestamp feature/locater later.
def dt5(taskmasters):
    pass

# Function to add tasks
def add(newtask):
    f = open('taskmaster.txt', 'a')
    f.write(newtask)
    f.write("\n")
    f.close()
    newtask = '"'+newtask+'"'
    print(f"Added task: {newtask}")
    
   
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
    try:
        ud()
        length = len(d)
        k = length
        for i in d:
            sys.stdout.buffer.write(f"[{length}] {d[length]}")
            sys.stdout.buffer.write("\n")
            length = length - 1
    except Exception as e:
        raise e
 
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
        sys.stdout.buffer.write("You have no pending tasks")

# Main block of code
if __name__ == '__main__':
    try:
        d = {}
        don = {}
        args = sys.argv
        if(args[1] == 'delete'):
            args[1] = 'delete'
        if(args[1] == 'add' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing todo string. Nothing added!")
 
        elif(args[1] == 'delete' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing numberBER for deleting todo.")
        else:
            globals()[args[1]](*args[2:])
 
    except Exception as e:
 
 # Commands Section - Defines the commands the user can input.
        x = """Task Master 3000 Commands:
task add "task name"  		# Adds new tasks
task show               	# Show all remaining tasks
task delete "task number"   # Delete a todo
"""
        sys.stdout.buffer.write(x)