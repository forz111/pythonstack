def check(string):  # определяем функцию check с аргументом string
    brackets_open = ('(', '[', '{', '<')  # определяем открывающие скобки
    brackets_closed = (')', ']', '}', '>')  # определяем закрывающие скобки
    stack = []  # создаем пустой стек
    for i in string:  # проходим по каждому символу в строке
        if i in brackets_open:  # если символ является открывающей скобкой
            stack.append(i)  # добавляем его в стек
        if i in brackets_closed:  # если символ является закрывающей скобкой
            if len(stack) == 0:  # если стек пустой
                return False  # возвращаем False
            index = brackets_closed.index(i)  # находим индекс закрывающей скобки
            open_bracket = brackets_open[index]  # находим соответствующую открывающую скобку
            if stack[-1] == open_bracket:  # если последний элемент в стеке является открывающей скобкой
                stack.pop()  # удаляем его из стека
            else:
                return False  # возвращаем False
    return not stack  # возвращаем True, если стек пустой, иначе False


string = input()  # запрашиваем у пользователя ввод строки
print(check(string))  # выводим результат проверки строки на правильность расстановки скобок

