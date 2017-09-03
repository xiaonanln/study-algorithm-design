
from DFS import DFS
from DFSOrders import DFSOrders

class TopologicalSorting(DFSOrders):

	def __init__(self, g):
		assert g.directed, 'must be digraph'
		super(TopologicalSorting, self).__init__(g)
		self.onStack = [False] * g.V
		self.isDAG = True

	def order(self):
		return list(reversed(self.postOrder))

	def run(self):
		DFSOrders.run(self)
		print 'postOrder', self.postOrder

	def dfs(self, u):
		self.marked[u] = True
		self.onStack[u] = True

		for v in self.g.adj[u]:
			if not self.marked[v]:
				self.dfs(v)
			elif self.onStack[v]: # back edge detected
				self.isDAG = False

		self.postOrder.append(u)
		self.onStack[u] = False


if __name__ == '__main__':
	from Graph import Graph
	g = Graph(5, directed=True)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 4)
	g.addEdge(4, 3)

	# g.addEdge()
	ts = TopologicalSorting(g)
	ts.run()
	print 'isDAG', ts.isDAG
	print ts.order()
