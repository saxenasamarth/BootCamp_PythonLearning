from datetime import date
class person:
	def __init__(self,name,age):
		self.name =name
		self.age=age

	def get_name(self):
		return self.name

	@classmethod   # can only access class level variables
	def fromBirthYear(cls, name , year):
		return cls(name , date.today().year- year)

	@staticmethod
	def isAdult(age):
		return age>18

		def __str__(self):
			return "Age is {}and name is {}".format(self.age, self.name)


person1 =person('federer',37)
person2 =person.fromBirthYear('federer', 1981)

person.isAdult(20)


