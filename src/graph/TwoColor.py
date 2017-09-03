
from DFS import DFS

WHITE = 0
BLACK = 1

def complement(color):
	return 1 - color

class TwoColor(DFS):

	def __init__(self, g):
		super(TwoColor, self).__init__(g)
		self.hasCycle = False
		self.color = [-1] * g.V
		self.isBipartite = True

	def twocolor(self):
		for v in xrange(g.V):
			if not self.finished and self.color[v] == -1:
				self.dfs(v, WHITE)

	def dfs(self, u, color):
		self.color[u] = color

		for v in self.g.adj[u]:
			if self.finished:
				return

			if self.color[v] == -1:
				self.dfs(v, complement(color))
			elif self.color[v] == color:
				print  'Vertex %d and %d are both color %d' % (u, v, color)
				self.isBipartite = False

if __name__ == '__main__':
	from Graph import Graph
	g = Graph(5, directed=True)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	# g.addEdge()
	tw = TwoColor(g)
	tw.twocolor()
	print tw.color
	print 'isBipartite', tw.isBipartite
