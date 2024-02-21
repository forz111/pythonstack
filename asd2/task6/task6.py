import heapq


def read_adj_matrix_from_file(file_name):
    with open(file_name, 'r') as file:
        num_vertices = int(file.readline().strip())
        adj_matrix = [[int(x) for x in line.strip().split()] for line in file.readlines()]
    return num_vertices, adj_matrix


def create_graph_from_adj_matrix(num_vertices, adj_matrix):
    class Graph:
        def __init__(self, num_vertices, adj_matrix):
            self.num_vertices = num_vertices
            self.adj_matrix = adj_matrix

        def get_neighbors(self, vertex):
            neighbors = []
            for i in range(self.num_vertices):
                if self.adj_matrix[vertex][i] == 1:
                    neighbors.append(i)
            return neighbors

    return Graph(num_vertices, adj_matrix)


def write_mst_to_file(mst, file_name):
    with open(file_name, 'w') as file:
        for edge in mst:
            file.write(f"{edge[0]} {edge[1]}\n")


def kruskal(graph):
    num_vertices = graph.num_vertices
    mst = []
    rank = {i: 0 for i in range(num_vertices)}
    parent = {i: i for i in range(num_vertices)}

    def find(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find(parent[vertex])
        return parent[vertex]

    def union(vertex1, vertex2):
        root1 = find(vertex1)
        root2 = find(vertex2)

        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph.adj_matrix[i][j] == 1:
                edges.append(((i, j), i, j))

    heapq.heapify(edges)

    while edges:
        _, vertex1, vertex2 = heapq.heappop(edges)
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            mst.append((vertex1, vertex2))

    return mst


num_vertices, adj_matrix = read_adj_matrix_from_file('graph.txt')
graph = create_graph_from_adj_matrix(num_vertices, adj_matrix)
mst = kruskal(graph)
write_mst_to_file(mst, 'mst.txt')
