class shape():
	def __init__(self):
		pass

	def getArea(self):
		return 0


class square(shape):
	def __init__(self,l):
		self.length=l

	def getArea(self):
		return self.length*self.length



sq=square(5)
print(sq.getArea())


sp=shape()
print(sp.getArea())