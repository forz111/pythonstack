# Функция для проверки, является ли граф эйлеровым
# Функция для проверки, является ли граф эйлеровым
def is_eulerian(graph):
    # Подсчитываем количество вершин с нечетной степенью
    odd = 0
    for row in graph:
        degree = sum(row)
        if degree % 2 == 1:
            odd += 1
    # Граф эйлеров, если нет вершин с нечетной степенью
    return odd == 0


# Функция для проверки, является ли ребро мостом в графе
def is_bridge(graph, u, v):
    # Копируем граф
    graph_copy = [row[:] for row in graph]
    # Удаляем ребро из копии графа
    graph_copy[u][v] = 0
    graph_copy[v][u] = 0
    # Проверяем, связен ли граф после удаления ребра
    visited = [False] * len(graph)
    dfs(graph_copy, u, visited)
    return not visited[v]


# Функция для обхода графа в глубину
def dfs(graph, v, visited):
    # Помечаем вершину как посещенную
    visited[v] = True
    # Перебираем соседние вершины
    for u in range(len(graph)):
        if graph[v][u] == 1 and not visited[u]:
            # Рекурсивно обходим соседнюю вершину
            dfs(graph, u, visited)


# Функция для нахождения эйлерова цикла в графе
def find_eulerian_cycle(graph):
    # Проверяем, является ли граф эйлеровым
    if not is_eulerian(graph):
        return None
    # Количество вершин в графе
    n = len(graph)
    # Стек для хранения текущего пути
    stack = []
    # Список для хранения эйлерова цикла
    cycle = []
    # Начинаем с произвольной вершины (например, с нулевой)
    stack.append(0)
    # Пока стек не пуст
    while stack:
        # Берем вершину из стека
        v = stack.pop()
        # Пока есть непосещенные ребра из этой вершины
        while any(graph[v]):
            # Находим первое такое ребро и проверяем, является ли оно мостом
            for u in range(n):
                if graph[v][u] == 1:
                    if is_bridge(graph, v, u):
                        break
                    else:
                        # Удаляем ребро из графа и добавляем новую вершину в стек
                        graph[v][u] = 0
                        graph[u][v] = 0
                        stack.append(u)
                        break
        # Добавляем вершину в цикл
        cycle.append(v)
    # Возвращаем цикл в обратном порядке
    return cycle[::-1]


file_path = "graph.txt"


def read_adjacency_matrix(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        graph = []
        for line in lines:
            row = [int(x) for x in line.split()]
            graph.append(row)
    return graph


graph = read_adjacency_matrix(file_path)

# Находим и выводим эйлеров цикл или сообщаем, что его нет
cycle = find_eulerian_cycle(graph)
with open('output.txt', 'w', encoding='utf-8') as f:
    if cycle:
        f.write("Эйлеров цикл:", cycle)
    else:
        f.write("Граф не является эйлеровым")
