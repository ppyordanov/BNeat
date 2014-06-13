'''
#organizer v1
#author: P. Yordanov
#date: 13.06.2014

'''

#imports
import os.path

#global vars
myt = []
mytt = ""
c = 1

#instructions
instructions = "\nWelcome to BNeat v1 \n\n1. press 'q' to quit \n2. press 'v' to view today's tasks \n3. press 'a' to add a new task \n4. press 'e' to edit task list \n5. press 'l' to load a task list from a file\n6. press 's' to save today's task list"

#function definitions
def validate(input):
	if(os.path.isfile(input)):
		return True
	return False

def view_tasks():
	global mytt, myt
	print myt
	if(mytt == ""):
		print "No tasks added today.. :("
		return
	print mytt

def add_task():
	global mytt, c
	tinput = raw_input("\nEnter task content: ")
	task = str(c) + ". " + tinput
	mytt += "\n" + task
	myt.append(task)
	print "task saved.."
	c +=1

def edit_tasks():
	global myt
	c = 0
	for t in myt:
		print t
		c+=1
	if(c == 0):
		print "no tasks"
		return
	edit = int(input("\nEnter task number to edit: "))
	if(edit > c or edit <=0):
		print "invalid input"

	newc = raw_input("\nEnter new task content: ")
	myt[c-1] = str(c) + ". " + newc

	print "task edited.."

def load_tasks():
	global mytt
	file = raw_input("\nFile to load (.txt): ")
	if(validate(file) is False):
		print "invalid file"
		return
	f = open(file, 'r')

	print "\nFile loaded. Displaying contents:\n\n"

	mytt += "\n"
	for line in f:
		print line
		mytt += line

def save_tasks():
	file = raw_input("\nFile to save (.txt): ")
	if(validate(file) is False):
		print "invalid file"
		#return

	f = open(file,  'w+')
	f.write(mytt)
	print "Tasks saved.."

def proc_input(uinput):

	if(uinput == 'q'):
		print "See ya."
	elif(uinput == 'v'):
		view_tasks()
	elif(uinput == 'a'):
		add_task()
	elif(uinput == 'e'):
		edit_tasks()
	elif(uinput == 'l'):
		load_tasks()
	elif(uinput == 's'):
		save_tasks()
	elif(uinput == 'h'):
		print instructions
	else:
		print "I didn't quite get that. Try again or press 'h' for help."

#welcome screen
print instructions

uinput = ''

while(uinput != 'q'):
	uinput = raw_input("\nMake your choice: ")
	proc_input(uinput)

quit()