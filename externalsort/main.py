def sort_large_file(file_path):
    # Создаем временные файлы для хранения отсортированных данных
    temp_files = split_sort_file(file_path)

    # Сливаем отсортированные файлы в один
    merge_files(temp_files, file_path)


def split_sort_file(file_path):
    temp_files = []
    with open(file_path, 'r') as file:
        for chunk in read_in_chunks(file):
            sorted_chunk = sorted(chunk)
            temp_file = write_to_temp_file(sorted_chunk)
            temp_files.append(temp_file)
    return temp_files


def read_in_chunks(file, chunk_size=1024):
    while True:
        data = list(map(int, file.readlines(chunk_size)))
        if not data:
            break
        yield data


def write_to_temp_file(sorted_data):
    temp_file = open('temp_file.txt', 'w+')
    temp_file.writelines('\n'.join(map(str, sorted_data)))
    temp_file.seek(0)
    return temp_file


def merge_files(files, output_path):
    with open(output_path, 'w') as output_file:
        while files:
            min_file = min(files, key=get_current_line)
            output_file.write(get_current_line(min_file))
            advance_file(min_file)
            if get_current_line(min_file) is None:
                files.remove(min_file)


def get_current_line(file):
    pos = file.tell()
    line = file.readline()
    file.seek(pos)
    return line


def advance_file(file):
    file.readline()


sort_large_file('large_file.txt')
