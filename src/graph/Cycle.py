
from DFS import DFS

class Cycle(DFS):

	def __init__(self, g):
		assert not g.directed, 'not work for digraph'
		super(Cycle, self).__init__(g)
		self.hasCycle = False

	run = DFS.dfsall

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
	g = Graph(3)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(2, 1)
	# g.addEdge()
	hc = Cycle(g)
	hc.run()
	print hc.hasCycle
