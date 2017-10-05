class Edge(object):
	def __init__(self, u, v):
		self.u = u
		self.v = v
		self.weight = None

	def printEdge(self):
		print "(%s, %s), Weight: %s" % (self.u.getName(), self.v.getName(), self.weight)
	def equals(self, edge):
		if self.u.getName() == edge.u.getName() and self.v.getName() == edge.v.getName():
			return True
		else:
			return False