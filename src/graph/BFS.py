from collections import deque

class BFS(object):
	def __init__(self, graph):
		self.g = graph
		self.parent = [-1] * graph.V
		self.marked = [False] * graph.V
		self.visited = [False] * graph.V
		self.q = deque()

	def bfs(self, s):
		q, g, marked, visited = self.q, self.g, self.marked, self.visited

		q.append(s)
		marked[s] = True

		while q:
			u = q.popleft()
			self.visitVertex(u)
			visited[u] = True

			for v in g.adj[u]:
				if not visited[v] or g.directed:
					self.visitEdge(u, v)

				if not marked[v]:
					self.parent[v] = u
					marked[v] = True
					q.append(v)

	def bfsall(self):
		for v in xrange(self.g.V):
			if not self.marked[v]:
				self.bfs(v)

	def visitVertex(self, v):
		pass

	def visitEdge(self, u, v):
		pass

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
	bfs = BFS(g)
	bfs.bfs(0)
	bfs.bfs(2)
	print l
	print bfs.hasPathTo(3), bfs.hasPathTo(2)
	print bfs.getPath(3)
	print bfs.getPath(0)
	print bfs.getPath(2)

