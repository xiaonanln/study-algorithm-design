
import random
from collections import deque

class Graph(object):

    def __init__(self, V, directed=False):
        self.V = V
        self.directed = directed
        self.adj = [deque() for _ in xrange(V)]
        self.E = 0

    def addEdge(self, v1, v2):
        self.E += 1
        self.adj[v1].append(v2)
        if not self.directed:
            self.adj[v2].append(v1)

    def edges(self):
        if self.directed:
            for u, adj in enumerate(self.adj):
                for v in adj:
                    yield (u, v)
        else:
            for u, adj in enumerate(self.adj):
                for v in adj:
                    if v > u: break
                    yield (u, v)

    def __reversed__(self):
        g = Graph(self.V, directed=self.directed)
        for u in xrange(self.V):
            for v in self.adj[u]: # edge u -> v
                g.addEdge(v, u)

        return g