class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def iterativePreorder(root):
    if root is None:
        return

    stack = []
    stack.append(root)

    traversal = ""

    while stack:
        node = stack.pop()
        traversal += str(node.val) + " "

        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)

    return traversal


def createTree(tree_str):
    stack = []
    i = 0
    while i < len(tree_str):
        if tree_str[i] != '(' and tree_str[i] != ')' and tree_str[i] != ',' and tree_str[i] != ' ':
            j = i
            while j < len(tree_str) and tree_str[j] != '(' and tree_str[j] != ')' and tree_str[j] != ',' and tree_str[
                j] != ' ':
                j += 1
            node = Node(int(tree_str[i:j]))
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
            i = j
        elif tree_str[i] == ')':
            stack.pop()
            i += 1
        else:
            i += 1
    return stack[0] if stack else None


tree_str = input("Введите бинарное дерево в формате линейно-скобочной записи: ")

root = createTree(tree_str)

print("Прямой обход: ", iterativePreorder(root))
