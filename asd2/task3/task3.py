import queue


# Функция для чтения графа из файла
def read_graph_from_file(file_name):
    with open(file_name, 'r') as file:
        graph = []
        for line in file:
            # Проверка, является ли строка числовой
            if line.replace(' ', '').replace('\n', '').isdigit():
                graph.append(list(map(int, line.split())))
    return graph


# Функция для записи компонент связности в файл
def write_components_to_file(file_name, components):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f'Количество компонент связности: {len(components)}\n')
        for i, component in enumerate(components, 1):
            file.write(f'Компонента связности {i}: {" ".join(map(str, component))}\n')


# Функция для выполнения обхода в ширину (BFS) графа
def bfs(graph, start_vertex):
    n = len(graph)
    visited = [False for _ in range(n)]
    visited[start_vertex] = True
    q = queue.Queue()
    q.put(start_vertex)

    component = [start_vertex]

    while not q.empty():
        v = q.get()
        for i in range(n):
            if graph[v][i] and not visited[i]:
                visited[i] = True
                q.put(i)
                component.append(i)

    return component, visited


# Функция для определения компонент связности в графе
def find_components(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    components = []

    for v in range(n):
        if not visited[v]:
            component, visited = bfs(graph, v)
            components.append(component)

    return components


# Главная функция
def main():
    graph = read_graph_from_file('graph.txt')
    components = find_components(graph)
    write_components_to_file('components.txt', components)


# Вызов главной функции
main()
