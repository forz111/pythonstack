# сортировка пузырьком

def bubbleSort(array):
    swapped = False
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array


alist = input('Сортировка пузырьком: ').split()
alist = [int(x) for x in alist]
bubbleSort(alist)
print('Отсортированный список: ', end='')
print(alist)
