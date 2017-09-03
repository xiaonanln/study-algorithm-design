
from DFS import DFS

class DFSOrders(DFS):

	def __init__(self, graph):
		super(DFSOrders, self).__init__(graph)
		self.preOrder = []
		self.postOrder = []
		self.reversePostOrder = []

	def dfs(self, u):
		self.marked[u] = True

		for v in self.g.adj[u]:
			if self.finished:
				return

			if not self.marked[v]:
				self.parent[v] = u
				self.dfs(v)

		self.visited[u] = True

	def dfsall(self):
		for v in xrange(self.g.V):
			if not self.finished and not self.marked[v]:
				self.dfs(v)
