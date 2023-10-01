def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделение массива на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивное применение сортировки слиянием к двум половинам
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Слияние отсортированных половин
    merged = merge(left_half, right_half)

    return merged


def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Слияние двух отсортированных массивов
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Добавление оставшихся элементов из левого массива (если есть)
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Добавление оставшихся элементов из правого массива (если есть)
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


arr = [int(x) for x in input().split()]
sorted_arr = merge_sort(arr)
print(sorted_arr)
