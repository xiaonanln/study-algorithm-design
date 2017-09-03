
from DFS import DFS

class DFSOrders(DFS):

	def __init__(self, graph):
		super(DFSOrders, self).__init__(graph)
		self.preOrder = []
		self.postOrder = []

	def dfs(self, u):
		self.marked[u] = True
		self.preOrder.append(u)

		for v in self.g.adj[u]:
			if not self.marked[v]:
				self.dfs(v)

		self.postOrder.append(u)

	def dfsall(self):
		for v in xrange(self.g.V):
			if not self.finished and not self.marked[v]:
				self.dfs(v)

	def run(self):
		self.dfsall()

if __name__ == '__main__':
	from Graph import Graph
	g = Graph(5, directed=True)

