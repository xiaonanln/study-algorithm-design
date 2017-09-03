
from DFS import DFS

class TopologicalSorting(DFS):

	def __init__(self, g):
		super(TopologicalSorting, self).__init__(g)
		self.sorted = []

	def isDAG(self):
		pass

	def order(self):
		pass

	def topologicalSort(self):
		for u in xrange(self.g.V):
			if not self.marked[u]:
				self.dps(u)

	def dfs(self, u):
		self.marked[u] = True

		for v in self.g.adj[u]:
			if not self.marked[v]:
				self.dfs(v)

if __name__ == '__main__':
	from Graph import Graph
	g = Graph(5, directed=True)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	# g.addEdge()
	tw = TwoColor(g)
	tw.twocolor()
	print tw.color
	print 'isBipartite', tw.isBipartite
