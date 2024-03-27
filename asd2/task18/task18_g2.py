def subset_sum(numbers, target):
  """
  Решает задачу о сумме подмножеств с помощью динамического программирования и
  возвращает подмножество, сумма которого равна target.

  Аргументы:
    numbers: список чисел.
    target: целевая сумма.

  Возвращает:
    Список чисел, составляющих подмножество с суммой target,
    или None, если такого подмножества не существует.
  """

  n = len(numbers)
  dp = [[False] * (target + 1) for _ in range(n + 1)]

  # Базовый случай: если target равен 0, то пустое подмножество является решением
  for i in range(n + 1):
    dp[i][0] = True

  # Заполняем таблицу dp
  for i in range(1, n + 1):
    for j in range(1, target + 1):
      if numbers[i - 1] <= j:
        dp[i][j] = dp[i - 1][j - numbers[i - 1]] or dp[i - 1][j]
      else:
        dp[i][j] = dp[i - 1][j]

  # Восстанавливаем подмножество
  if dp[n][target]:
    subset = []
    i = n
    j = target
    while i > 0 and j > 0:
      if not dp[i - 1][j]:
        subset.append(numbers[i - 1])
        j -= numbers[i - 1]
      i -= 1
    return subset
  else:
    return None

# Пример использования
numbers = [3, 9, 8, 4, 5, 7, 10]
target = 50

subset = subset_sum(numbers, target)

if subset:
  print("Подмножество с суммой", target, ":", subset)
else:
  print("Не существует подмножества с суммой", target)