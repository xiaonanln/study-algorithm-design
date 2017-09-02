
from DFS import DFS

class CheckCycle(DFS):

	def __init__(self, g):
		super(CheckCycle, self).__init__(g)
		self.hasCycle = False

	def checkcycle(self):
		for v in xrange(g.V):
			if not self.marked[v]:
				self.dfs(v)

	def visitEdge(self, u, v):
		print 'visitEdge', u, v
		print u, v, self.parent[v]
		if self.parent[v] != u:
			self.hasCycle = True

if __name__ == '__main__':
	from Graph import Graph
	g = Graph(5)
	g.addEdge(0, 1)
	g.addEdge(1, 2)
	g.addEdge(3, 4)
	g.addEdge(2, 0)
	hc = CheckCycle(g)
	hc.checkcycle()
	print hc.hasCycle
