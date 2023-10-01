def quicksort(arr):
    if len(arr) <= 1:
        return arr

    opor = arr[len(arr) // 2]  # Выбор опорного элемента
    left = [x for x in arr if x < opor]  # Элементы меньше опорного
    middle = [x for x in arr if x == opor]  # Элементы равные опорному
    right = [x for x in arr if x > opor]  # Элементы больше опорного

    return quicksort(left) + middle + quicksort(right)  # Рекурсивное применение быстрой сортировки


# Пример использования:
arr = [int(i) for i in input().split()]
sorted_arr = quicksort(arr)
print(sorted_arr)
