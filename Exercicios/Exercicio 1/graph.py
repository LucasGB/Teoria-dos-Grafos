from vertex import Vertex
from edge import Edge

class Graph(object):
	def __init__(self):
		self.vertexes = []
		self.edges = []

	def add_vertex(self, name):	
		if len(self.vertexes) == 0: 
			v = Vertex(name)
			self.vertexes.append(v)
			return
		else:
			for vertex in self.vertexes:			
				if(vertex.equals(name)):
					return False

		v = Vertex(name)
		self.vertexes.append(v)

	def add_edge(self, u, v):
		self.add_vertex(u)
		self.add_vertex(v)

		e = Edge(u, v)
		self.edges.append(e)

	def loadGraphFromFile(self, FILE):
		with open(FILE, 'r') as f:
			for line in f:
				u, v = line.strip().split(' ')
				self.add_edge(u, v)

		for v in self.vertexes:
			print "a"+v.name

		print "Tam:",len(self.vertexes)