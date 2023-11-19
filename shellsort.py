# сортировка Шелла

def shellSort(alist):
    n = len(alist)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            j = i
            while j >= step and alist[j] < alist[j - step]:
                alist[j], alist[j - step] = alist[j - step], alist[j]
                j = j - step
        step = step // 2


alist = input('Сортировка Шелла: ').split()
alist = [int(x) for x in alist]
shellSort(alist)
print('Отсортированный список: ', end='')
print(alist)
