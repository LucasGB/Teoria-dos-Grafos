from vertex import Vertex
from edge import Edge

class Graph(object):
	def __init__(self):
		self.vertexes = []
		self.edges = []

	def add_vertex(self, name):	
		for vertex in self.vertexes:			
			if(vertex.equals(name)):
				return vertex

		vertex = Vertex(name)
		self.vertexes.append(vertex)

		return vertex

	def add_edge(self, u, v):
		u = self.add_vertex(u)
		v = self.add_vertex(v)

		e = Edge(u, v)

		for edge in self.edges:
			if(e.equals(edge)):
				return

		self.edges.append(e)

	def printVertexes(self):
		for v in self.vertexes:
			print v.getName()
		print "Total number of vertexes:", len(self.vertexes)

	def printEdges(self):
		for e in self.edges:
			e.printEdge()
		print "Total number of edges:", len(self.edges)

	def loadGraphFromFile(self, FILE):
		with open(FILE, 'r') as f:
			for line in f:
				u, v = line.strip().split(' ')
				self.add_edge(u, v)

		self.printVertexes()
		self.printEdges()