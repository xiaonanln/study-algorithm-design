
from BFS import BFS

class CC(BFS):

	def __init__(self, g):
		super(CC, self).__init__(g)
		self.id = [-1] * g.V
		self.count = 0

	def cc(self):
		for v in xrange(g.V):
			if not self.marked[v]:
				self.bfs(v)
				self.count += 1

	def connected(self, u, v):
		"""check if u and v is connected"""
		return self.id[u] == self.id[v]

	def visitVertex(self, v):
		self.id[v] = self.count

if __name__ == '__main__':
	from Graph import Graph
	g = Graph(5)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(3, 4)
	cc = CC(g)
	cc.cc()
	print cc.count
	print cc.id
	print cc.connected(0, 3)
