import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def best_first_search(self, start, goal):
        visited = set()
        priority_queue = [(0, start)]

        while priority_queue:
            (cost, current_node) = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            print(current_node, end=" ")
            visited.add(current_node)

            if current_node == goal:
                return True

            for neighbor, neighbor_cost in self.graph.get(current_node, []):
                if neighbor not in visited:
                    heuristic = neighbor_cost
                    heapq.heappush(priority_queue, (heuristic, neighbor))

        return False

# g graph oluşturulur ve düğümler eklenir
g = Graph()
g.add_edge("A", [("B", 3), ("C", 5)])
g.add_edge("B", [("D", 2), ("E", 4)])
g.add_edge("C", [("F", 1)])
g.add_edge("D", [])
g.add_edge("E", [])
g.add_edge("F", [])

print("Best-First Search ile gezilen düğümler:")
result = g.best_first_search("A", "E")

if result:
    print("\nHedef düğüm bulundu.")
else:
    print("\nHedef düğüm bulunamadı.")
