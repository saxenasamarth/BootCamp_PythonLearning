import time
class person:
	def __init__(self, name):
		self.__name = name
	def __get_time(self):
		return time.time()
	def get_name(self):
		print('Name is {} and time is {}'.format(self.__name, self.__get_time()))

p=person("Sachin")
p.get_name()
#p.__get_time() --> this methos will fail as __get_time is a private method.