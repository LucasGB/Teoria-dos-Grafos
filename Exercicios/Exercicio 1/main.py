from graph import Graph
from dijkstra import Dijkstra

if __name__ == '__main__':
	graph = Graph()
	graph.loadGraphFromFile('entrada.txt')
	graph.debug()

	dijkstra = Dijkstra(graph, graph.get_vertex('a'), graph.get_vertex('d'))
	path = dijkstra.run()

	print '\nShortest Path:', path

