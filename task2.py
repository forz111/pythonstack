def check_brackets(expression):
    """
    Функция проверяет корректность расстановки скобок в выражении.
    :param expression: строка с математическим выражением
    :return: True, если скобки расставлены корректно, иначе False
    """
    stack = []  # создаем пустой стек
    for char in expression:
        if char == '(':  # если символ - открывающая скобка, добавляем ее в стек
            stack.append(char)
        elif char == ')':  # если символ - закрывающая скобка, проверяем, что последняя открывающая скобка в стеке
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()  # если все хорошо, удаляем последнюю открывающую скобку из стека
    return len(stack) == 0  # если в стеке не осталось скобок, значит все скобки были закрыты корректно

def to_postfix(expression):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    postfix = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            postfix.append(expression[i:j])
            i = j - 1
        elif char in priority:
            while stack and stack[-1] in priority and priority[stack[-1]] >= priority[char]:
                postfix.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if not stack or stack[-1] != '(':
                raise ValueError('Incorrect expression')
            stack.pop()
        i += 1
    while stack:
        if stack[-1] in '()':
            raise ValueError('Incorrect expression')
        postfix.append(stack.pop())
    return postfix

def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        elif token in '+-*/':
            if len(stack) < 2:
                raise ValueError('Incorrect expression')
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ValueError('Division by zero')
                stack.append(a / b)
    if len(stack) != 1:
        raise ValueError('Incorrect expression')
    return stack[0]

def calculate(expression):
    if not check_brackets(expression):
        raise ValueError('Incorrect expression')
    postfix = to_postfix(expression[:-1])
    return evaluate_postfix(postfix)

expression = '2+7*(9/3)-5='
result = calculate(expression)
print(result)