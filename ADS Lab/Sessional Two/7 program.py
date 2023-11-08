from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def bfs(self, start_vertex):
        visited = [False] * self.num_vertices
        queue = deque()
        queue.append(start_vertex)
        visited[start_vertex] = True

        print("Breadth-First Traversal:")
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in range(self.num_vertices):
                if self.adj_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

# Create a graph with 5 vertices
num_vertices = 5
g = Graph(num_vertices)

# Add edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 2)

# Define the starting vertex for BFS
start_vertex = 0

g.bfs(start_vertex)
