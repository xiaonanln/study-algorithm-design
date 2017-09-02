
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
