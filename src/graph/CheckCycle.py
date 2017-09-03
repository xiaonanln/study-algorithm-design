
from DFS import DFS

class CheckCycle(DFS):

	def __init__(self, g):
		super(CheckCycle, self).__init__(g)
		self.hasCycle = False

	def checkcycle(self):
		for v in xrange(g.V):
			if not self.finished and not self.marked[v]:
				self.dfs(v)

	def dfs(self, u):
		self.marked[u] = True

		for v in self.g.adj[u]:
			if self.finished:
				return

			if not self.marked[v]:
				self.parent[v] = u
				self.dfs(v)
			elif self.parent[u] != v:
				print 'Fond cycle: %d -> ... -> %d -> %d' % (v, u, v)
				self.hasCycle = True
				self.finished = True

if __name__ == '__main__':
	from Graph import Graph
	g = Graph(5, directed=True)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(2, 3)

	g.addEdge(3, 0)
	# g.addEdge()
	hc = CheckCycle(g)
	hc.checkcycle()
	print hc.hasCycle
