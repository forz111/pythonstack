def find_euler_tour(graph):
    # Создаем пустой список для хранения тура
    tour = []

    # Создаем список ребер графа
    # Для каждой вершины u в графе мы проходим по всем вершинам v
    # Если между вершинами u и v есть ребро (graph[u][v] == 1), то добавляем пару (u, v) в список ребер E
    E = [(u, v) for u in range(len(graph)) for v in range(len(graph)) if graph[u][v]]

    # Создаем список степеней вершин графа
    # Для каждой вершины u в графе мы проходим по всем вершинам v
    # Если между вершинами u и v есть ребро (graph[u][v] == 1), то увеличиваем степень вершины u на 1
    numEdges = [sum(1 for v in range(len(graph)) if graph[u][v]) for u in range(len(graph))]

    # Проверяем, что все вершины имеют четную степень и список ребер не пуст
    # Если это так, то начинаем поиск тура с первой вершины
    # В противном случае возвращаем None, так как Эйлеров цикл не существует
    if all(num % 2 == 0 for num in numEdges) and E:
        find_tour(E[0][0], E, tour, numEdges)
        tour.reverse()
        return tour
    else:
        return None

def find_tour(u, E, tour, numEdges):
    # Проходим по всем ребрам графа
    for (a, b) in E:
        # Если текущая вершина совпадает с одним из концов ребра
        if a == u:
            # Удаляем ребро из списка ребер
            E.remove((a, b))
            # Уменьшаем степень соответствующих вершин
            numEdges[a] -= 1
            numEdges[b] -= 1
            # Продолжаем поиск тура с другого конца ребра
            find_tour(b, E, tour, numEdges)
        # Если текущая вершина совпадает с другим концом ребра
        elif b == u:
            # Удаляем ребро из списка ребер
            E.remove((a, b))
            # Уменьшаем степень соответствующих вершин
            numEdges[a] -= 1
            numEdges[b] -= 1
            # Продолжаем поиск тура с другого конца ребра
            find_tour(a, E, tour, numEdges)
    # Добавляем текущую вершину в тур
    tour.append(u)

def main():
    # Открываем файл для чтения
    with open('graph2.txt', 'r', encoding='utf-8') as f:
        # Читаем матрицу смежности из файла
        graph = [list(map(int, line.split())) for line in f]
    # Находим Эйлеров тур
    tour = find_euler_tour(graph)
    # Открываем файл для записи
    with open('output4.txt', 'w', encoding='utf-8') as f:
        # Если Эйлеров тур существует, то записываем его в файл
        # В противном случае записываем сообщение о том, что Эйлеров цикл не существует
        if tour is not None:
            for node in tour:
                f.write(str(node) + '\n')
        else:
            f.write("Эйлеров цикл не существует в данном графе.\n")

main()
