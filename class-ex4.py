#inheritance
class Animal(object):

   def __init__(self, name):
       self.name = name

   def getName(self):
       return self.name

   def isMammal(self):
       return False

   def isHerbivore(self):
   		return False

class foodHabit:
	def isHerbivore(self):
		return True

class Panda(Animal,foodHabit):   #inherits from 2 classes

   def isMammal(self):
       return True




p=Panda("panda1")

print(p.isMammal())
print(p.getName())
print(p.isHerbivore())
