from vertex import Vertex
from edge import Edge

class Graph(object):
	def __init__(self):
		self.vertexes = []
		self.edges = []

	# Returns edges
	def get_edges(self, vertex):
		adj = []

		for e in self.edges:
			if(e.getU() == vertex):
				adj.append(e)

		return adj

	def get_vertex(self, name):
		for vertex in self.vertexes:
			if(vertex.equals(name)):
				return vertex


	def add_vertex(self, name):	
		for vertex in self.vertexes:			
			if(vertex.equals(name)):
				return vertex

		vertex = Vertex(name)
		self.vertexes.append(vertex)

		return vertex

	def add_edge(self, u, v, w):
		u = self.add_vertex(u)
		v = self.add_vertex(v)

		e = Edge(u, v, int(w))

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
				u, v, w = line.strip().split(' ')
				self.add_edge(u, v, w)

	def debug(self):
		self.printVertexes()
		self.printEdges()