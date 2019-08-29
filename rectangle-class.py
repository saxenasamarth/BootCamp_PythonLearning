class rectangle():
	def __init__(self,l,w):
		self.length=l
		self.width=w


	def getArea(self):
		return self.length*self.width


r=rectangle(5,4)
print(r.getArea())