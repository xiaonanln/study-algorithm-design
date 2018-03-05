

class Graph(object):
	def __init__(self, V):
		self.adj = [[] for _ in xrange(V)]
		self.V = V
		self.E = 0

	def addEdge(self, v, w):
		self.adj[v].append(w)
		self.adj[w].append(v)

