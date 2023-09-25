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