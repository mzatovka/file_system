from write_file import*
from read_file import search_user
import os

# Задание. найти файл config.txt . 

# if os.path.exists("config.txt"):
#     print('файл найден')
# else:
#      with open("config.txt", "w", encoding="utf-8") as file:
#          print('файл создан')  # можно удалить принт и вместо него написать pass . Всё будет работать


    


# with open("config.txt", "a", encoding="utf-8") as file:
#     pass


append_film('titanic',9.9)




#Программа запрашивает у пользователя имя папки и имя файла . Создаёт папку (если её нет )

# name_dir = input('введите имя папки: ')
# name_file = input('введите имя файла: ')
# if os.path.exists(name_dir): 
#     with open(name_file, "a", encoding="utf-8") as file:
#         pass
# else: 
#     with open(name_dir, "a", encoding="utf-8") as file:
#         pass
        
#os.mkdir(name_dir)

# print(name_dir in  os.listdir('.')) # проверка есть ли название папки которое мы введём в name_dir во всех директориях
 
# if name_dir in  os.listdir('.'):
#      with open(f'{name_dir}/{name_file}', "a", encoding="utf-8") as file:
#         pass
# else:
#     os.mkdir(name_dir)
#     with open(f'{name_dir}/{name_file}', "a", encoding="utf-8") as file:
#         pass


# if name_dir not in os.listdir('.'):
#     os.mkdir(name_dir)

# with open(name_dir + '/' + name_file, 'a', encoding='utf-8') as file:
#     pass

    
    

    




# wtite_user_message('привет') 


# append_new_user()


# search_name = input('Какого пользователя хотите найти? ')
# print(f'пользователь {search_name} находится на {search_user(search_name)} строчке')












 




# file = open('data.txt', 'r', encoding='utf-8')


# for line in file :
#     print(line.strip())


#content = file.read()   чтение всего файла


#print(content)


# file.close()


# with open ('data/new_data.txt','r', encoding='utf-8') as file: 
#     lines = file.readlines()
    
    
#     print(lines)
    
    
#     for index, line in enumerate(lines, start = 1):
#         print(f'{index}-{line.strip()}
        
        
#     print(len(lines))    
    
        
