
from heap.PriorityQueue import PriorityQueue

INFINITY = float('inf')

class PrimPQ(object):

	def __init__(self, graph):
		assert not graph.directed
		self.g = graph
		self.intree = [False] * graph.V
		self.distance = [INFINITY] * graph.V
		self.distancePQ = PriorityQueue(graph.V)
		self.parent = [-1] * graph.V

	def run(self, s):
		u = s
		while u != -1:
			self.intree[u] = True
			print '%d -> %d' % (self.parent[u], u)

			for v, w in self.g.adj[u]:
				if not self.intree[v] and w < self.distance[v]:
					oldDist = self.distance[v]
					self.distance[v] = w
					self.parent[v] = u
					if oldDist == INFINITY:
						self.distancePQ.push(v, -w)
					else:
						self.distancePQ.change(v, -w)

			# find next u
			if self.distancePQ:
				u = self.distancePQ.pop()
				# print 'pop', u
			else:
				u = -1

if __name__ == '__main__':
	from WeightedGraph import WeightedGraph
	g = WeightedGraph(5)
	g.addEdge(0, 1, 1)
	g.addEdge(0, 2, 2)
	g.addEdge(2, 3, 3)
	g.addEdge(2, 4, 1)
	g.addEdge(0, 4, 3)
	g.addEdge(3, 4, 4)
	prim = PrimPQ(g)
	prim.run(0)
