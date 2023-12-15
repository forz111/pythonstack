import heapq
import os

# Размер буфера для сортировки в памяти
BUFFER_SIZE = 1000


def external_multiway_merge_sort(input_file, output_file):
    # Фаза деления
    temp_files = split_phase(input_file)

    # Фаза слияния
    merge_phase(temp_files, output_file)

    # Удаление временных файлов
    for file in temp_files:
        os.remove(file)


def split_phase(input_file):
    temp_files = []
    with open(input_file, 'r') as file:
        temp_array = []
        count = 0
        for line in file:
            temp_array.append(int(line))
            count += 1
            if count >= BUFFER_SIZE:
                temp_array.sort()  # Сортировка в памяти
                temp_file = f"temp{len(temp_files)}.txt"
                with open(temp_file, 'w') as temp:
                    temp.write('\n'.join(map(str, temp_array)))
                temp_files.append(temp_file)
                temp_array = []
                count = 0
        if temp_array:
            temp_array.sort()  # Сортировка в памяти
            temp_file = f"temp{len(temp_files)}.txt"
            with open(temp_file, 'w') as temp:
                temp.write('\n'.join(map(str, temp_array)))
            temp_files.append(temp_file)
    return temp_files


def merge_phase(temp_files, output_file):
    min_heap = []
    for file in temp_files:
        temp = open(file, 'r')
        first_number = int(temp.readline().strip())
        min_heap.append((first_number, temp))

    heapq.heapify(min_heap)

    with open(output_file, 'w') as output:
        while min_heap:
            minValue, temp = heapq.heappop(min_heap)
            output.write(str(minValue) + '\n')
            next_number = temp.readline().strip()
            if next_number:
                heapq.heappush(min_heap, (int(next_number), temp))
            else:
                temp.close()
    return


# Пример использования
external_multiway_merge_sort('input12.txt', 'output12.txt')