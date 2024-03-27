def subset_sum(numbers, target):
    # Сортируем числа в порядке убывания
    numbers.sort(reverse=True)

    # Инициализируем список для хранения результата
    result = []

    # Инициализируем переменную для хранения текущей суммы
    current_sum = 0

    # Проходим по всем числам
    for number in numbers:
        # Если текущая сумма плюс текущее число меньше или равна целевому значению
        if current_sum + number <= target:
            # Добавляем число в результат
            result.append(number)
            # Увеличиваем текущую сумму
            current_sum += number

    # Если текущая сумма равна целевому значению, возвращаем результат
    if current_sum == target:
        return result
    # В противном случае, возвращаем None
    else:
        return None


numbers = [1, 2, 3, 4, 5]
target = 15
print(subset_sum(numbers, target))  # Вывод: [5, 4]
