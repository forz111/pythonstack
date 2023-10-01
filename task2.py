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
