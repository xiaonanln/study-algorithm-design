
import random
from BaseGraph import BaseGraph


class Graph(BaseGraph):

    def addEdge(self, v1, v2):
        self.E += 1
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)

if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 4)
    g.addEdge(1, 3)

    l = []
    g.BFS(lambda v: l.append(v))
    print l
