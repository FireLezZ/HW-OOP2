import os

def merge_files(file_names, output_file):
    files_info = []
    
    # Читаем содержимое каждого файла и добавляем информацию в список
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.readlines()
            files_info.append((file_name, len(content), content))
    
    # Сортируем список по количеству строк в каждом файле
    files_info.sort(key=lambda x: x[1])
    
    # Записываем отсортированные данные в результирующий файл
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for file_info in files_info:
            result_file.write(f"{file_info[0]}\n{file_info[1]}\n")
            result_file.writelines(file_info[2])
            result_file.write('\n')

file_names = ['1.txt', '2.txt', '3.txt']  
output_file = 'result.txt'

merge_files(file_names, output_file)
