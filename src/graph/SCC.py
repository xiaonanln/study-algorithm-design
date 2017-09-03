
from DFS import DFS
from DFSOrders import DFSOrders

class SCC(DFS):

	def __init__(self, graph):
		assert graph.directed, "must be digraph"
		DFS.__init__(self, graph)
		self.id = [-1] * graph.V
		self.count = 0

	def isStronglyConnected(self, u, v):
		return self.id[u] == self.id[v]

	def run(self):
		gr = reversed(self.g)
		dfsOrders = DFSOrders(gr)
		dfsOrders.run()
		for v in reversed(dfsOrders.postOrder):
			if not self.marked[v]:
				self.dfs(v)
				self.count += 1

	def dfs(self, u):
		self.marked[u] = True
		self.id[u] = self.count

		for v in self.g.adj[u]:

			if not self.marked[v]:
				self.parent[v] = u
				self.dfs(v)

if __name__ == '__main__':
	from Graph import Graph
	g = Graph(5, directed=True)
	g.addEdge(0, 1)
	g.addEdge(1, 2)
	g.addEdge(2, 0)

	scc = SCC(g)
	scc.run()
	print scc.count
	print scc.id


