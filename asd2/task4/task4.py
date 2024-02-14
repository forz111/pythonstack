def dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_vertex)
    for vertex in graph[start_vertex] - visited:
        dfs(graph, vertex, visited)
    return visited


def find_components(graph):
    visited = set()
    components = []
    for vertex in graph:
        if vertex not in visited:
            component = dfs(graph, vertex)
            visited.update(component)
            components.append(component)
    return components


def read_graph_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        graph = {}
        for i, line in enumerate(file):
            graph[i] = {j for j, cell in enumerate(map(int, line.split())) if cell}
    return graph


def write_components_to_file(file_name, components):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f'Количество компонент связности: {len(components)}\n')
        for i, component in enumerate(components, 1):
            file.write(f'Компонента связности {i}: {" ".join(map(str, component))}\n')


def main():
    graph = read_graph_from_file('graph.txt')
    components = find_components(graph)
    write_components_to_file('components.txt', components)


main()
