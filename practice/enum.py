#!/usr/bin/env python
def enum(**enums):
	return type('Enum', (), enums)

Gender = enum(MALE=0, FEMALE=1, UNSPECIFIED=2)

class User:
	name = ""
	age = 0
	gender = Gender.UNSPECIFIED

	def display(self):
		if (self.gender == Gender.MALE):
			print self.name, 'is a male'
		elif (self.gender == Gender.FEMALE):
			print self.name, 'is a female'
		else:
			print self.name, 'did not specificy a gender'

user1 = User()
user1.name = 'Mike'
user1.gender = Gender.MALE

user2 = User()
user2.name = 'Sally'
user2.gender = Gender.FEMALE

user1.display()
user2.display() 
