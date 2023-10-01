<<<<<<< HEAD
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
=======
from random import randint


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    x = arr[randint(0, len(arr) - 1)]
    left = [i for i in arr if i < x]
    mid = [i for i in arr if i == x]
    right = [i for i in arr if i > x]
    return quick_sort(left) + mid + quick_sort(right)


def dot_in_a(d, arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > d:
            right = mid - 1
        elif arr[mid] <= d:
            left = mid + 1
    return right + 1


def dot_in_b(d, arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= d:
            right = mid - 1
        elif arr[mid] < d:
            left = mid + 1
    return right + 1


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
dots = list(map(int, input().split()))


a = quick_sort([i[0] for i in ab])
b = quick_sort([i[1] for i in ab])

for i in dots:
    print(dot_in_a(i, a) - dot_in_b(i, b), end=' ')
>>>>>>> origin/master
