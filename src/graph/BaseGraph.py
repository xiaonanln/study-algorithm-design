


from collections import deque

class BaseGraph(object):

    def __init__(self, V):
        self.V = V
        self.adj = [deque() for _ in xrange(V)]
        self.E = 0

    def BFS(self, f):
        visited = [False for _ in xrange(self.V)]
        q = deque()

        def bfs(u):
            if visited[u]:
                return

            q.append(u)
            visited[u] = True

            while q:
                u = q.popleft()
                f(u)

                for v in self.adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)

        for u in xrange(self.V):
            bfs(u)

    def DFS(self, f):
        visited = [False for _ in xrange(self.V)]
        q = deque()

        def dfs(u):
            if visited[u]:
                return

            q.append(u)
            visited[u] = True

            while q:
                u = q.popleft()
                f(u)

                for v in self.adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)

        for u in xrange(self.V):
            dfs(u)

