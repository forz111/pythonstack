import queue

# Функция для выполнения обхода в ширину (BFS) графа
def bfs(graph, start_vertex):
    n = len(graph)  # количество вершин в графе
    distances = [-1 for _ in range(n)]  # инициализация списка расстояний
    distances[start_vertex] = 0  # расстояние от начальной вершины до себя равно 0
    q = queue.Queue()  # создание очереди для BFS
    q.put(start_vertex)  # добавление начальной вершины в очередь

    # Пока очередь не пуста
    while not q.empty():
        v = q.get()  # извлечение вершины из очереди
        # Для каждой вершины, смежной с v
        for i in range(n):
            # Если вершина i смежна с v и еще не была посещена
            if graph[v][i] and distances[i] == -1:
                distances[i] = distances[v] + 1  # обновление расстояния до i
                q.put(i)  # добавление i в очередь

    return distances  # возвращение списка расстояний

# Функция для чтения графа из файла
def read_graph_from_file(file_name):
    with open(file_name, 'r') as file:
        # Чтение каждой строки файла и преобразование ее в список целых чисел
        graph = [list(map(int, line.split())) for line in file]
    return graph  # возвращение графа

# Функция для записи расстояний в файл
def write_distances_to_file(file_name, distances):
    with open(file_name, 'w') as file:
        # Запись каждого расстояния в файл
        for distance in distances:
            file.write(str(distance) + '\n')

# Главная функция
def main():
    graph = read_graph_from_file('graph.txt')  # чтение графа из файла
    distances = bfs(graph, 0)  # выполнение BFS для графа
    write_distances_to_file('distances.txt', distances)  # запись расстояний в файл

# Вызов главной функции
main()
