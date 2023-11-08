from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Create a graph
g = Graph()

# Add edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Define the starting vertex for DFS
start_vertex = 0

print("Depth-First Traversal (Starting from vertex 0):")
visited = set()
g.dfs(start_vertex, visited)
