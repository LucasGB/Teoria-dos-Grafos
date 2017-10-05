class Vertex(object):
	def __init__(self, name):
		self.name = name

	def equals(self, name):
		return True if self.name == name else False

	def getName(self):
		return self.name