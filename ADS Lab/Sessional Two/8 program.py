from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, vertex, visited, component):
        visited[vertex] = True
        component.append(vertex)

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, component)

    def connected_components(self):
        visited = [False] * len(self.graph)
        components = []

        for vertex in self.graph:
            if not visited[vertex]:
                component = []
                self.dfs(vertex, visited, component)
                components.append(component)

        return components

# Create a graph
g = Graph()

# Add edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(3, 4)

# Get the connected components
connected_components = g.connected_components()

# Display the connected components
print("Connected Components:")
for component in connected_components:
    print(component)
