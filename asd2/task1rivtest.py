from functools import cmp_to_key

def orientation(p, q, r):
    '''
    Определяет ориентацию p, q и r (счётчиковое или по часовой стрелке)
    '''
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def merge(hull1, hull2):
    '''
    Объединяет две выпуклые оболочки в одну
    '''
    n1 = len(hull1)
    n2 = len(hull2)

    # Находим самую правую точку в первой оболочке и самую левую точку во второй оболочке
    l = max(range(n1), key=lambda i: hull1[i][0])
    r = min(range(n2), key=lambda i: hull2[i][0])

    # Начинаем с самой правой точки первой оболочки и двигаемся против часовой стрелки,
    # пока не достигнем самой левой точки второй оболочки
    upper = [(l, r)]
    while True:
        succ = (r+1) % n2
        if orientation(hull1[l], hull2[r], hull2[succ]) == 2:
            r = succ
        else:
            break
        if r == upper[0][1]:  # Добавлено условие выхода
            break
    upper.append((l, r))

    # Теперь двигаемся по часовой стрелке от самой левой точки второй оболочки до самой правой точки первой оболочки
    lower = [(l, r)]
    while True:
        pred = (l-1) % n1
        if orientation(hull1[l], hull2[r], hull1[pred]) == 1:
            l = pred
        else:
            break
        if l == lower[0][0]:  # Добавлено условие выхода
            break
    lower.append((l, r))

    # Объединяем верхнюю и нижнюю оболочки
    hull = []
    l, r = upper[0]
    while True:
        hull.append(hull1[l])
        if upper[0] == upper[1] and lower[0] == lower[1]:
            break
        l_succ = (l+1) % n1
        if upper[0] != upper[1]:
            if lower[0] == lower[1] or orientation(hull1[l], hull1[l_succ], hull2[r]) == 1:
                l = l_succ
                upper[0] = (l, r)
            else:
                r = (r+1) % n2
                lower[0] = (l, r)
        else:
            r = (r+1) % n2
            lower[0] = (l, r)
        if l == upper[0][0] and r == upper[0][1]:  # Добавлено условие выхода
            break

    return hull


def convex_hull(points):
    '''
    Строит выпуклую оболочку с помощью алгоритма "разделяй и властвуй"
    '''
    n = len(points)

    # Если количество точек меньше 3, выпуклая оболочка не может быть построена
    if n < 3:
        return points

    # Сортируем точки по x-координате
    points.sort(key=cmp_to_key(lambda p, q: p[0] - q[0] if p[0] != q[0] else p[1] - q[1]))

    # Разделяем точки на две половины
    mid = n // 2
    left = points[:mid]
    right = points[mid:]

    # Рекурсивно строим выпуклые оболочки для каждой половины
    hull1 = convex_hull(left)
    hull2 = convex_hull(right)

    # Объединяем две оболочки в одну
    hull = merge(hull1, hull2)

    return hull

points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
print(convex_hull(points))

