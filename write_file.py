# w - режим перезаписи файла (старое содержимое удаляет)
#with open('result.txt', 'w', encoding='utf-8') as file:
#    file.write('Привет мир\n')
#    file.write('hello world')




#with open('result.txt','a',encoding = 'utf-8') as file:
    #file.write('новая запись')
    
    
    

def wtite_user_message(message):
    with open('result.txt', 'w',encoding='utf-8') as file:
        file.write(f'письмо от юзера: {message}')
    print('сообщение добавлено')
    
    
def append_new_user():
    count_user = int(input('сколько юзеров добавить? '))
    
    with open('data/users.txt', 'a',  encoding='utf-8') as file:
        for i in range(count_user):
            name = input(f'введите имя юзера ')
            file.write(name + '\n')
            
            
            
def append_favorite_film():
    with open('data/favorite_film.txt', 'a',   encoding='utf-8') as file:
        append_film = input('введите название фильма ')
        file.write(append_film)
    print('фильм добавлен ')
        
        
#append_favorite_film()        


def read_file():
    with open('data/favorite_film.txt' , 'r' , encoding='utf-8') as file:
         films = file.readlines()
         for number, film in enumerate(films, start = 1):
            print(f'{number} - {film.strip()} ')
            
read_file()