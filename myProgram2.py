import myProgram

class Point:
	def __init__(self):
		self.foo = 11
		self._bar = 23
		self.__baz = 44
		
		
myPoint = Point()

print(dir(myPoint))