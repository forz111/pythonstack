def is_connected(graph):
    # Начинаем с вершины 0
    start_node = 0
    # Создаем список для отслеживания посещенных вершин
    color = [0] * len(graph)
    # Помечаем начальную вершину как посещенную
    color[start_node] = 1
    # Создаем стек и добавляем в него начальную вершину
    stack = [start_node]
    # Пока стек не пуст
    while stack:
        # Берем вершину из стека
        node = stack[-1]
        stack.pop()
        # Перебираем все вершины графа
        for i in range(len(graph)):
            # Если есть ребро и вершина еще не была посещена
            if graph[node][i] == 1 and color[i] == 0:
                # Добавляем вершину в стек и помечаем ее как посещенную
                stack.append(i)
                color[i] = 1
    # Если все вершины были посещены, то граф связный
    return 0 not in color

def is_eulerian(graph):
    # Подсчитываем количество вершин с нечетной степенью
    odd = 0
    for row in graph:
        degree = sum(row)
        if degree % 2 == 1:
            odd += 1
    # Граф эйлеров, если нет вершин с нечетной степенью
    return odd == 0

def find_euler_tour(graph):
    # Проверяем, является ли граф связным и эйлеровым
    if not is_connected(graph) or not is_eulerian(graph):
        return None
    # Находим вершину с нечетной степенью или, если такой нет, начинаем с вершины 0
    u = next((i for i, v in enumerate(graph) if sum(v) % 2 == 1), 0)
    # Создаем стек и путь
    stack = [u]
    path = []
    # Пока стек не пуст
    while stack:
        # Берем вершину из стека
        u = stack[-1]
        # Если у вершины есть соседи
        if any(graph[u]):
            # Находим первого соседа
            v = graph[u].index(1)
            # Удаляем ребро между u и v
            graph[u][v] = graph[v][u] = 0
            # Добавляем вершину в стек
            stack.append(v)
        else:
            # Если у вершины нет соседей, добавляем ее в путь и удаляем из стека
            path.append(stack.pop())
    # Возвращаем перевернутый путь
    return path[::-1]

def main():
    # Открываем файл для чтения
    with open('graph.txt', 'r', encoding='utf-8') as f:
        # Читаем матрицу смежности из файла
        graph = [list(map(int, line.split())) for line in f]
    # Находим Эйлеров тур
    tour = find_euler_tour(graph)
    # Открываем файл для записи
    with open('output3.txt', 'w', encoding='utf-8') as f:
        # Если Эйлеров тур существует, то записываем его в файл
        # В противном случае записываем сообщение о том, что Эйлеров цикл не существует
        if tour is not None:
            for node in tour:
                f.write(f"->{str(node)}")
        else:
            f.write("Эйлеров цикл не существует в данном графе.\n")

main()
