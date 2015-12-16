#!/usr/bin/env python
import sys

#User class
class User:
	name = ""
	age = 0
	height = 0
	weight = 0

	def save(self, f):
		f.write(self.name + '\n')
		f.write(str(self.age) + '\n')
		f.write(str(self.height) + '\n')
		f.write(str(self.weight) + '\n')

	def loadFromFile(self, f):
		self.name = f.readline().rstrip()
		self.age = int(f.readline())
		self.height = float(f.readline())
		self.weight = int(f.readline())

	def loadFromInput(self):
		self.name = raw_input('Enter User Name (Q to exit): ')

		if self.name == 'Q':
			return

		self.age = int(raw_input('Enter Age: '))
		self.height = float (raw_input('Enter Height (in feet): '))
		self.weight = int(raw_input('Enter Weight: '))

	def display(self):
		print ''
		print 'User Information:'
		print 'User Name  :', self.name
		print 'User Age   :', self.age
		print 'User Height:', self.height
		print 'User Weight:', self.weight

#main program code
users = []

def createUsers():
	while 1:
		u = User()
		u.loadFromInput()

		if u.name == 'Q':
			break
		
		users.append(u)

def saveUsers():
	f = open('users.info', 'w')
	f.write(str(len(users)) + '\n')

	for u in users:
		u.save(f)

	f.close()

def readUsers():
	f = open('users.info', 'r')
	num = int(f.readline())

	for i in range(num):
		u = User()
		u.loadFromFile(f)
		users.append(u)

	f.close()

def displayUsers():
	for u in users:
		u.display()

if len(sys.argv) > 1 and sys.argv[1] == 'READ':
	readUsers()
else:
	createUsers()
	saveUsers()

displayUsers()	
