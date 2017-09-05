
import operator
# from heap.PriorityQueue import PriorityQueue
from unionfind.UnionFind import UnionFind
from sorting.QuickSortW3 import QuickSortW3

class Kruskal(object):

	def __init__(self, graph):
		assert not graph.directed
		self.g = graph
		self.vuf = UnionFind(graph.V)
		self.intree = [False] * graph.V
		self.parent = [-1] * graph.V

	def run(self, s):
		edges = list(self.g.edges())
		edges.sort(key=operator.itemgetter(2))

		for u, v, w in edges:
			if self.vuf.find(u) != self.vuf.find(v):
				print '%d -> %d W %d' % (u, v, w)
				self.vuf.union(u, v)

if __name__ == '__main__':
	from graph.WeightedGraph import WeightedGraph
	g = WeightedGraph(5)
	g.addEdge(0, 1, 1)
	g.addEdge(0, 2, 2)
	g.addEdge(2, 3, 3)
	g.addEdge(2, 4, 1)
	# g.addEdge(0, 4, 3)
	# g.addEdge(3, 4, 4)
	prim = Kruskal(g)
	prim.run(0)
