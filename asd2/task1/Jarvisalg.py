def leftmost_point(points):
    '''
    Находит самую левую точку
    '''
    left_most = 0
    for i in range(1, len(points)):
        if points[i][0] < points[left_most][0]:
            left_most = i
        elif points[i][0] == points[left_most][0]:
            if points[i][1] > points[left_most][1]:
                left_most = i
    return left_most


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


def convex_hull(points):
    n = len(points)

    # Если количество точек меньше 3, выпуклая оболочка не может быть построена
    if n < 3:
        return

    # Находим самую левую точку
    l = leftmost_point(points)

    hull = []
    p = l
    q = None

    while True:
        hull.append(points[p])
        q = (p + 1) % n

        for r in range(n):
            if orientation(points[p], points[q], points[r]) == 2:
                q = r

        p = q

        if p == l:
            break

    return hull


points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
print(convex_hull(points))

# points = [
#     (0, 0),
#     (1, -4),
#     (-1, -5),
#     (-5, -3),
#     (-3, -1),
#     (-1, -3),
#     (-2, -2),
#     (-1, -1),
#     (-2, -1),
#     (-1, 1)
# ]