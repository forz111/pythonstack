def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read().replace('\n', '')
    return data

def hash_function(text, table_size):
    hash_sum = 0
    for i in range(len(text)):
        hash_sum += ord(text[i]) * i
    return hash_sum % table_size

def build_hash_table(text, table_size):
    hash_table = [[] for _ in range(table_size)]
    words = text.split(' ')
    for word in words:
        hash_value = hash_function(word, table_size)
        if len(hash_table[hash_value]) == 0:
            hash_table[hash_value] = [word]
        else:
            found_empty_slot = False
            for i in range(1, table_size):
                next_index = (hash_value + i) % table_size
                if len(hash_table[next_index]) == 0:
                    hash_table[next_index] = [word]
                    found_empty_slot = True
                    break
            if not found_empty_slot:
                hash_table[hash_value].append(word)
    return hash_table

def write_hash_table(hash_table, file_name):
    with open(file_name, 'w') as file:
        for row in hash_table:
            file.write(str(row) + '\n')

if __name__ == "__main__":
    text = read_file("input13.txt")
    table_size = int(input())
    hash_table = build_hash_table(text, table_size)
    write_hash_table(hash_table, "output13.txt")