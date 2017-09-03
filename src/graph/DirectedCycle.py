
from DFS import DFS

class DirectedCycle(DFS):

	def __init__(self, g):
		assert g.directed, 'not a digraph'
		super(DirectedCycle, self).__init__(g)
		self.hasCycle = False
		self.onStack = [False] * g.V

	def run(self):
		self.dfsall()

	def dfs(self, u):
		self.marked[u] = True
		self.onStack[u] = True

		for v in self.g.adj[u]:
			if self.finished:
				return

			print '%d -> %d marked=%s onStack=%s' % (u, v, self.marked[v], self.onStack[v])
			if not self.marked[v]:
				self.parent[v] = u
				self.dfs(v)
			elif self.onStack[v]: # onStack check is the key to find cycle in digraph!!!
				path = [v, u]
				while self.parent[u] != v:
					u = self.parent[u]
					path.append(u)

				path.append(v)
				path = list(reversed(path))

				print 'Fond cycle: %s' % path
				self.hasCycle = True
				self.finished = True

		self.onStack[u] = False

if __name__ == '__main__':
	from Graph import Graph
	g = Graph(4, directed=True)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 3)
	g.addEdge(3, 0)

	# g.addEdge()
	hc = DirectedCycle(g)
	hc.run()
	print hc.hasCycle
