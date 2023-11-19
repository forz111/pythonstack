# сортировка вставками

def insertionSort(alist):
    N = len(alist)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
            else:
                break


alist = input('Сортировка вставками: ').split()
alist = [int(x) for x in alist]
insertionSort(alist)
print('Отсортированный список: ', end='')
print(alist)
