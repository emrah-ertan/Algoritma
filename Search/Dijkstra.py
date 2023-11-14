import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start):
        distance = {node: float('inf') for node in self.graph}
        distance[start] = 0
        visited = set()
        priority_queue = [(0, start)]

        while priority_queue:
            (current_distance, current_node) = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            for (neighbor, weight) in self.graph[current_node]:
                distance_through_current = current_distance + weight

                if distance_through_current < distance[neighbor]:
                    distance[neighbor] = distance_through_current
                    heapq.heappush(priority_queue, (distance[neighbor], neighbor))

        return distance

# g graph oluşturulur ve düğümler eklenir
g = Graph()
g.add_edge("A", "B", 2)
g.add_edge("A", "C", 4)
g.add_edge("B", "C", 1)
g.add_edge("B", "D", 7)
g.add_edge("C", "D", 3)
g.add_edge("D", "E", 2)
g.add_edge("E", "A", 2)

start_node = "A"
distances = g.dijkstra(start_node)

for node, distance in distances.items():
    print(f"En kısa yol {start_node} ile {node} arasında {distance} birim uzaklıktadır.")
