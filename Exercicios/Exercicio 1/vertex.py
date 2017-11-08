class Vertex(object):
	def __init__(self, name):
		self.name = name

	def equals(self, name):
		return True if self.name == name else False

	def getName(self):
		return self.name

	def setD(self, d):
		self.d = d

	def getD(self):
		return self.d

	def setPi(self, pi):
		self.pi = pi

	def getPi(self):
		return self.pi