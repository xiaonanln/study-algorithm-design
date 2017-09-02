
from BaseGraph import BaseGraph


class DGraph(BaseGraph):

    def addEdge(self, v1, v2):
        self.E += 1
        self.adj[v1].append(v2)

if __name__ == '__main__':
    g = DGraph(5)
    g.addEdge(0, 4)
    g.addEdge(0, 1)
    g.addEdge(1, 3)

    l = []
    g.BFS(0, lambda v: l.append(v))
    print l

    l = []
    g.BFS(1, lambda v: l.append(v))
    print l
