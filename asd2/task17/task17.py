# Функция для решения задачи о ящиках и элементах
def pack_elements(elements, capacity):
    # Сортируем элементы по убыванию веса
    elements.sort(reverse=True)
    # Создаем список для хранения ящиков
    boxes = []
    # Проходим по всем элементам
    for element in elements:
        # Проверяем, есть ли свободное место в последнем ящике
        if boxes and boxes[-1] + element <= capacity:
            # Добавляем элемент в последний ящик
            boxes[-1] += element
        else:
            # Открываем новый ящик и кладем туда элемент
            boxes.append(element)
            # Возвращаем список ящиков
    return boxes


# Пример использования функции
elements = [4, 4, 6, 6, 1, 8, 9, 1, 4, 2, 1]
capacity = 10
boxes = pack_elements(elements, capacity)
print(f"Элементы: {elements}")
print(f"Вместимость: {capacity}")
print(f"Ящики: {boxes}")
print(f"Количество ящиков: {len(boxes)}")