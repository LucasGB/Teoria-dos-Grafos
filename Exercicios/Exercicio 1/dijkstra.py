


class Dijkstra(object):
	def __init__(self, graph, S, T):
		self.graph = graph
		self.S = S
		self.T = T
		self.visited = []
		self.path = []

	def extract_min(self):
		min_d = None

		for v in self.Q:
			if(min_d == None):
				min_d = v

			elif(v.getD() < min_d.getD()):
				min_d = v

		return min_d

	def initialize(self):
		for v in self.graph.vertexes:
			v.setD(float('inf'))
			v.setPi(None)

		self.S.setD(0)
		self.Q = set(self.graph.vertexes)

	def run(self):
		self.initialize()

		while(len(self.Q) != 0):
			u = self.extract_min()
			self.Q.remove(u)
			self.visited.append(u)

			for e in self.graph.get_edges(u):
				if(e.getV() not in self.visited and e.getV().getD() > u.getD() + e.getWeight()):
					e.getV().setD(e.getU().getD() + e.getWeight())
					e.getV().setPi(u)
					self.Q.add(e.getV())

		vertex = self.T
		self.path.append(vertex.getName())
		
		while(vertex.getPi() != None):
			vertex = vertex.getPi()
			self.path.append(vertex.getName())
	
		return self.path[::-1]