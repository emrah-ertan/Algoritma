from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = []

        visited.add(start)
        queue.append(start)

        while queue:
            start = queue.pop(0)
            print(start, end=" ")

            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# g graph oluşturulur ve düğümler eklenir
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS ile gezilen düğümler:")
g.bfs(2)
