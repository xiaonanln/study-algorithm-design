
import random
from BaseGraph import BaseGraph


class Graph(BaseGraph):

    def addEdge(self, v1, v2):
        self.E += 1
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)
