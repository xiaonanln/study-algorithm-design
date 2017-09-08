

inf = float('inf')

class Floyd(object):
	def __init__(self, G):
		self.G = G # Floyd works better on bit matrix, but we still use adjacency matrix
		V = G.V
		self.allPairsDistance = [[inf] * V for _ in xrange(V)]
		for u in xrange(V):
			for v, w in G.adj[u]:
				self.allPairsDistance[u][v] = w

	def run(self):
		G = self.G
		for k in xrange(G.V):
			for u in xrange(G.V):
				for v in xrange(G.V):
					self.allPairsDistance[u][v] = min(self.allPairsDistance[u][v], self.allPairsDistance[u][k] + self.allPairsDistance[k][v])


if __name__ == '__main__':

	from graph.WeightedGraph import WeightedGraph
	g = WeightedGraph(5)
	g.addEdge(0, 1, 1)
	g.addEdge(0, 2, 2)
	g.addEdge(2, 3, 3)

	g.addEdge(0, 4, 3)
	g.addEdge(2, 4, 1)
	g.addEdge(3, 4, 4)
	apmd = Floyd(g)

	print 'Before running Floyd: '
	for vec in apmd.allPairsDistance:
		print vec

	apmd.run()
	print 'After running Floyd: '
	for vec in apmd.allPairsDistance:
		print vec