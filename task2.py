<<<<<<< HEAD
# Функция, которая проверяет, является ли символ оператором
def is_operator(c):
    return c in "+-*/"

# Функция, которая возвращает приоритет оператора
def priority(c):
    if c in "+-":
        return 1
    elif c in "*/":
        return 2
    else:
        return 0

# Функция, которая преобразует инфиксное выражение в постфиксное
def to_postfix(expr):
    stack = []  # Стек для хранения операторов
    postfix = ""  # Строка для хранения постфиксного выражения
    for c in expr:
        if c.isdigit():  # Если символ - цифра, добавляем его в постфиксное выражение
            postfix += c
        elif is_operator(c):  # Если символ - оператор
            # Извлекаем операторы из стека, пока приоритет текущего оператора меньше или равен приоритету оператора на вершине стека
            while stack and is_operator(stack[-1]) and priority(stack[-1]) >= priority(c):
                postfix += stack.pop()
            stack.append(c)  # Добавляем текущий оператор в стек
        elif c == "(":  # Если символ - открывающая скобка, добавляем ее в стек
            stack.append(c)
        elif c == ")":  # Если символ - закрывающая скобка
            # Извлекаем операторы из стека, пока не встретим открывающую скобку
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            if stack and stack[-1] == "(":  # Удаляем открывающую скобку из стека
                stack.pop()
    # Извлекаем оставшиеся операторы из стека и добавляем их в постфиксное выражение
    while stack:
        postfix += stack.pop()
    return postfix

# Функция, которая вычисляет значение постфиксного выражения
def calculate(expr):
    stack = []  # Стек для хранения операндов
    for c in expr:
        if c.isdigit():  # Если символ - цифра, добавляем ее в стек
            stack.append(int(c))
        elif is_operator(c):  # Если символ - оператор
            b = stack.pop()  # Извлекаем два последних операнда из стека
            a = stack.pop()
            if c == "+":  # Выполняем соответствующую операцию и добавляем результат в стек
                stack.append(a + b)
            elif c == "-":
                stack.append(a - b)
            elif c == "*":
                stack.append(a * b)
            elif c == "/":
                if b == 0:  # Обрабатываем исключение деления на ноль
                    raise ValueError("division by zero")
                stack.append(a / b)
    return stack.pop()  # Возвращаем результат вычисления

expr = input().strip()  # Считываем входное выражение
postfix = to_postfix(expr)  # Преобразуем его в постфиксное выражение
result = calculate(postfix)  # Вычисляем значение постфиксного выражения
print(result)  # Выводим результат
=======
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
>>>>>>> origin/master
