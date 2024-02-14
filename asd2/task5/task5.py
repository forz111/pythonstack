def dfs(graph, vertex, visited, stack):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(vertex)

def dfs_t(graph, vertex, visited, component):
    visited.add(vertex)
    component.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_t(graph, neighbor, visited, component)

def transpose(graph):
    transposed = {vertex: [] for vertex in graph}
    for vertex in graph:
        for neighbor in graph[vertex]:
            transposed[neighbor].append(vertex)
    return transposed

def find_scc(graph):
    visited = set()
    stack = []
    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, visited, stack)

    transposed = transpose(graph)

    visited = set()
    scc = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            component = []
            dfs_t(transposed, vertex, visited, component)
            scc.append(component)
    return scc

def read_graph_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        graph = {}
        for i, line in enumerate(file):
            graph[i] = [j for j, cell in enumerate(map(int, line.split())) if cell]
    return graph

def write_scc_to_file(file_name, scc):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f'Количество сильно связных компонент: {len(scc)}\n')
        for i, component in enumerate(scc, 1):
            file.write(f'Сильно связная компонента {i}: {" ".join(map(str, component))}\n')

def main():
    graph = read_graph_from_file('graph.txt')
    scc = find_scc(graph)
    write_scc_to_file('scc.txt', scc)

main()
