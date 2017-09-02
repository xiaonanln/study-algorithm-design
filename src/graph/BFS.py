from collections import deque


class BFS(object):
	def __init__(self, graph, s):
		self.g = graph
		self.s = s

	def run(self, f):
		g, s = self.g, self.s
		marked = [False for _ in xrange(g.V)]
		q = deque()
		q.append(s)
		marked[s] = 1

		while q:
			u = q.popleft()
			f(u)

			for v in g.adj[u]:
				if not marked[v]:
					marked[v] = True
					q.append(v)

if __name__ == '__main__':
	from Graph import Graph

	g = Graph(5)
	g.addEdge(0, 4)
	g.addEdge(0, 1)
	g.addEdge(1, 3)

	l = []
	bfs = BFS(g, 0)
	bfs.run(lambda v: l.append(v))
	print l
