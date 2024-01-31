from collections import defaultdict

# Класс для представления графа
class Graph:

    # Конструктор для инициализации графа
    def __init__(self, vertices):
        self.V = vertices  # количество вершин
        self.graph = defaultdict(list)  # словарь, содержащий граф

    # Функция для добавления ребра в граф
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Функция для выполнения BFS из заданной вершины
    def BFS(self, v, visited):
        queue = []  # создаем очередь для BFS
        queue.append(v)  # помещаем текущую вершину в очередь
        visited[v] = True  # помечаем текущую вершину как посещенную

        while queue:  # пока очередь не пуста
            v = queue.pop(0)  # извлекаем вершину из очереди
            print(v, end=" ")

            # Получаем все смежные вершины текущей вершины v.
            # Если смежная вершина не была посещена, то помечаем ее
            # как посещенную и помещаем в очередь.
            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    # Функция для поиска всех компонент связности в графе
    def connectedComponents(self):
        visited = [False] * (self.V)  # помечаем все вершины как непосещенные
        cc = []  # список для хранения компонент связности
        for v in range(self.V):  # проходим по всем вершинам
            if visited[v] == False:  # если вершина не была посещена
                print("Component: ", end="")
                self.BFS(v, visited)  # выполняем BFS
                cc.append(v)  # добавляем вершину в список компонент связности
                print("\n")
        return cc

# Создаем граф
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
cc = g.connectedComponents()  # находим компоненты связности
print("Number of connected components:", len(cc))  # выводим количество компонент связности
