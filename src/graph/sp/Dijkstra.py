

class Dijkstra(object):

	def __init__(self, graph):
		assert not graph.directed
		self.g = graph
		self.intree = [False] * graph.V
		self.distance = [float('inf')] * graph.V
		self.parent = [-1] * graph.V

	def run(self, s):
		self.distance[s] = 0
		u = s
		while u != -1:
			self.intree[u] = True
			distu = self.distance[u]
			for v, w in self.g.adj[u]:
				if not self.intree[v] and distu + w < self.distance[v]:
					self.distance[v] = distu + w
					self.parent[v] = u

			# find next u
			u = -1
			mindist = float('inf')
			for v in xrange(self.g.V):
				if not self.intree[v] and self.distance[v] < mindist:
					mindist = self.distance[v]
					u = v

if __name__ == '__main__':
	from graph.WeightedGraph import WeightedGraph
	g = WeightedGraph(5)
	g.addEdge(0, 1, 1)
	g.addEdge(0, 2, 2)
	g.addEdge(2, 3, 3)
	g.addEdge(2, 4, 1)
	g.addEdge(0, 4, 3)
	g.addEdge(3, 4, 4)
	ds = Dijkstra(g)
	ds.run(0)
	print ds.distance
