
from BFS import BFS

class CC(BFS):

	def __init__(self, g):
		super(CC, self).__init__(g)
		self.id = [-1] * g.V
		self.count = 0

	def run(self):
		for v in xrange(g.V):
			if not self.marked[v]:
				self.bfs(v)
				self.count += 1

	def bfs(self, s):
		q, g, marked, visited = self.q, self.g, self.marked, self.visited

		q.append(s)
		marked[s] = True

		while q:
			u = q.popleft()
			self.id[u] = self.count
			visited[u] = True

			for v in g.adj[u]:
				if not marked[v]:
					self.parent[v] = u
					marked[v] = True
					q.append(v)

	def connected(self, u, v):
		"""check if u and v is connected"""
		return self.id[u] == self.id[v]

if __name__ == '__main__':
	from Graph import Graph
	g = Graph(5)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(3, 4)
	cc = CC(g)
	cc.run()
	print cc.count
	print cc.id
	print cc.connected(0, 3)
