class Node:
    def __init__(self, value):
        self.value = value   # значение узла
        self.left = None     # ссылка на левое поддерево
        self.right = None    # ссылка на правое поддерево

def build_tree_from_string(s):
    """
    Функция для построения бинарного дерева из строки в линейно-скобочной форме.
    Строка должна быть корректно сформирована.
    """
    stack = []  # Стек для отслеживания текущего пути в дереве
    root = None # корневой узел дерева
    i = 0       # индекс для итерации по строке

    while i < len(s):
        # Если текущий символ - число, создаем новый узел
        if s[i].isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            value = int(s[start:i])
            new_node = Node(value)

            # Если стек пуст, новый узел становится корневым
            if not stack:
                root = new_node
            else:
                # Иначе добавляем узел как левое или правое поддерево последнего узла в стеке
                parent = stack[-1]
                if not parent.left:
                    parent.left = new_node
                else:
                    parent.right = new_node

            stack.append(new_node)
            continue

        # Если встречаем закрывающую скобку, возвращаемся к предыдущему узлу
        elif s[i] == ')':
            stack.pop()

        i += 1

    return root

def insert(root, key):
    """
    Вставка нового узла в бинарное дерево поиска.
    """
    # Если корень пустой, создаем новый узел
    if root is None:
        return Node(key)

    # Рекурсивное добавление узла в соответствующее поддерево
    if key < root.value:
        root.left = insert(root.left, key)
    elif key > root.value:
        root.right = insert(root.right, key)

    return root

def minValue(node):
    """
    Поиск минимального значения в дереве.
    """
    current = node
    while current.left is not None:
        current = current.left
    return current.value

def delete_node(root, key):
    """
    Удаление узла из бинарного дерева поиска.
    """
    if root is None:
        return root

    # Рекурсивное удаление узла
    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # Если узел с двумя дочерними узлами, заменяем его минимальным узлом из правого поддерева
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        root.value = minValue(root.right)
        root.right = delete_node(root.right, root.value)

    return root

def search(root, key):
    """
    Поиск узла в бинарном дереве поиска.
    """
    # Если узел найден или дерево пустое, возвращаем узел
    if root is None or root.value == key:
        return root

    # Рекурсивный поиск в соответствующем поддереве
    if key < root.value:
        return search(root.left, key)
    else:
        return search(root.right, key)

def print_tree(root):
    """
    Вывод дерева в линейно-скобочной форме.
    """
    # Обработка пустого дерева
    if root is None:
        return "()"

    # Если у узла нет детей, выводим его значение
    if root.left is None and root.right is None:
        return f"({root.value})"

    # Рекурсивный вывод левого и правого поддеревьев
    left_subtree = print_tree(root.left)
    right_subtree = print_tree(root.right)

    return f"({root.value} {left_subtree} {right_subtree})"

def main():
    s = input("Введите бинарное дерево в линейно-скобочной форме: ")
    root = build_tree_from_string(s)

    while True:
        print("\n1. Добавить узел")
        print("2. Удалить узел")
        print("3. Найти узел")
        print("4. Показать дерево")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            value = int(input("Введите значение для добавления: "))
            root = insert(root, value)
        elif choice == '2':
            value = int(input("Введите значение для удаления: "))
            root = delete_node(root, value)
        elif choice == '3':
            value = int(input("Введите значение для поиска: "))
            node = search(root, value)
            if node:
                print("Узел найден")
            else:
                print("Узел не найден")
        elif choice == '4':
            print(print_tree(root))
        elif choice == '5':
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()

# 8 (3 (1, 6 (4, 7)), 10 (14 (13, ())))