

class Dijkstra(object):
	def __init__(self, graph, S):
		self.graph = graph
		self.S = S
		self.visited = []

	def extract_min(self):
		min_d = self.graph.vertexes[0]

		for v in self.Q:
			if(v.getD() < min_d.getD()):
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
				print e.getU().name
				if(e.getV().getD() > u.getD() + e.getWeight()):
					e.getV().setD(e.getU().getD() + e.getWeight())
					e.getV().setPi(u)
					self.Q.add(e.getV())

		print 'finished'



				