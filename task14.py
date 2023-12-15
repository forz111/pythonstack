import hashlib


# Определение хеш-функции
def get_hash(key):
    return hashlib.sha256(key.encode()).hexdigest()


# Открытие входного файла для чтения
with open('input14.txt', 'r') as file:
    # Чтение текста из файла
    text = file.read()

# Создание хеш-таблицы
hash_table = {}

# Разделение текста на слова
words = text.split()

# Заполнение хеш-таблицы
for word in words:
    # Вычисление хеша для ключа
    hash_key = get_hash(word)

    # Если ключ уже присутствует в таблице, добавляем значение в список
    if hash_key in hash_table:
        hash_table[hash_key].append(word)
    # Если ключа нет в таблице, создаем новый список с текущим значением
    else:
        hash_table[hash_key] = [word]

# Открытие результирующего файла для записи
with open('output14.txt', 'w') as file:
    # Запись хеш-таблицы в файл
    for key, value in hash_table.items():
        file.write(f"{key}: {', '.join(value)}\n")
