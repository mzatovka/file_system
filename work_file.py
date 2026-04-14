
import os
import shutil

print(os.path.exists("read_file.py")) # существует ли файл

if os.path.exists("read_file.py"): 
    print('файл существует')
    
    
    
#os.mkdir('reports/2026') # создаём папку (директорию)


print(os.listdir('.')) # выводит список файлов и папок


path = 'reports/2026'

print(os.path.isdir(path)) # проверка на то , является ли это папкой

print(os.path.isfile(path))  # проверка на то , является ли это файлом


shutil.rmtree(path)

#os.rmdir('reports/2026')

