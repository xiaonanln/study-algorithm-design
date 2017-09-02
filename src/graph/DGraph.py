
from .BaseGraph import BaseGraph


class DGraph(BaseGraph):

    def addEdge(self, v1, v2):
        self.E += 1
        self.adj[v1].append(v2)
