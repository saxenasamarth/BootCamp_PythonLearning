#class is an object and its variables are called attributes
# a function inisde class is called method
class Person:
	class_name="Person"
	def __init__(self,name):
	# this is a constructor
	 self.name=name


	def get_name(self):
		print('Name is', self.name)


p=Person('Samarth Saxena')
p.get_name()


#instance variable/ attributes

print(p.name)

#class variable/ attributes
print(Person.class_name)