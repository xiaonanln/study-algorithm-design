
import random
from collections import deque

class WeightedGraph(object):

    def __init__(self, V, directed=False):
        self.V = V
        self.directed = directed
        self.adj = [deque() for _ in xrange(V)]
        self.E = 0

    def addEdge(self, v1, v2, w):
        self.E += 1
        self.adj[v1].append( (v2, w) )
        if not self.directed:
            self.adj[v2].append( (v1, w) )

    def edges(self):
        if self.directed:
            for u, adj in enumerate(self.adj):
                for v, w in adj:
                    yield (u, v, w)
        else:
            for u, adj in enumerate(self.adj):
                for v, w in adj:
                    if v > u: break
                    yield (u, v, w)

    def __reversed__(self):
        g = WeightedGraph(self.V, directed=self.directed)
        for u in xrange(self.V):
            for v, w in self.adj[u]: # edge u -> v
                g.addEdge(v, u, w)

        return g