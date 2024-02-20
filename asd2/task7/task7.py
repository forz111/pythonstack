import sys
import heapq

def prim(graph, start_node):
    mst = []
    visited = [False] * len(graph)
    edges = [(0, start_node)]
    while edges:
        weight, node = heapq.heappop(edges)
        if not visited[node]:
            visited[node] = True
            mst.append(node)
            for edge, edge_weight in enumerate(graph[node]):
                if not visited[edge]:
                    heapq.heappush(edges, (edge_weight, edge))
    return mst

def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        graph = [[int(num) for num in line.split()] for line in file]
    return graph

def write_result_to_file(filename, result):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, result)))

def main():
    graph = read_graph_from_file('graph.txt')
    mst = prim(graph, 0)
    write_result_to_file('output.txt', mst)

if __name__ == "__main__":
    main()
