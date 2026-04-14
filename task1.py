
file = open('C:/проекты/работа с файлами/data/users.txt', 'r', encoding='utf-8')

line_input = input('введите имя : ')
for index, line in enumerate(file, start = 1):
    if line.strip() == line_input:
        print(f'{index}- {line}')
    
    
file.close()