import itertools

class AllPaths(object):
	def __init__(self, G):
		self.G = G

	def run(self, s, t):
		print 'Calculating All Paths From %s To %s:' % (s, t)

		G = self.G
		inpath = [False] * G.V
		path = [s]
		inpath[s] = True

		def bt():
			u = path[-1]
			if u == t:
				print path
				return

			for v in G.adj[u]:
				if not inpath[v]:
					path.append(v)
					inpath[v] = True
					bt()
					path.pop()
					inpath[v] = False

		bt()

if __name__ == '__main__':
	from graph.Graph import Graph
	G = Graph(5, directed=False)
	G.addEdge(0, 1)
	G.addEdge(0, 2)
	G.addEdge(0, 3)
	G.addEdge(0, 4)
	G.addEdge(1, 4)
	G.addEdge(2, 3)
	G.addEdge(3, 4)
	ap = AllPaths(G)
	ap.run(0, 4)
