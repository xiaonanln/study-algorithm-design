from collections import deque

class BFSPath(object):
	def __init__(self, graph, s):
		self.g = graph
		self.s = s
		self.parent = [-1] * g.V
		self.marked = [False] * g.V

	def run(self):
		g, s, marked = self.g, self.s, self.marked

		q = deque()
		q.append(s)
		marked[s] = 1

		while q:
			u = q.popleft()

			for v in g.adj[u]:
				if not marked[v]:
					self.parent[v] = u
					marked[v] = True
					q.append(v)

	def hasPathTo(self, v):
		return self.marked[v]

	def getPath(self, v):
		"""Get the path from s to v, inclusive"""
		if not self.marked[v]:
			return None

		path = []
		while v != -1:
			path.append(v)
			v = self.parent[v]

		return tuple(reversed(path))

if __name__ == '__main__':
	from Graph import Graph

	g = Graph(5)
	g.addEdge(0, 4)
	g.addEdge(0, 1)
	g.addEdge(1, 3)

	l = []
	bfs = BFSPath(g, 0)
	bfs.run()
	print l
	print bfs.hasPathTo(3), bfs.hasPathTo(2)
	print bfs.getPath(3)
	print bfs.getPath(0)
	print bfs.getPath(2)

