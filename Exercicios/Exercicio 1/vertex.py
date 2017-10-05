class Vertex(object):
	def __init__(self, name):
		self.name = name

	def equals(self, name):
		if self.name == name:
			return True			

	def getName(self):
		return self.name