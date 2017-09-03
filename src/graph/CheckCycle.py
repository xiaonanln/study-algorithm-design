
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
		print u, '->', v

	# def dfs(self, u):
	# 	self.marked[u] = True
	#
	# 	for v in self.g.adj[u]:
	# 		if not self.marked[v]:
	# 			self.parent[v] = u
	# 			self.dfs(v)
	# 		elif self.parent[u] != v:
	# 			self.hasCycle = True
	#
	# 	self.visited[u] = True

if __name__ == '__main__':
	from Graph import Graph
	g = Graph(5)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(2, 3)

	g.addEdge(3, 0)
	hc = CheckCycle(g)
	hc.checkcycle()
	print hc.hasCycle
