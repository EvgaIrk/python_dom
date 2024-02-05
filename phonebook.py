import os
def add_new_user(name:str,phone:str,filename:str):
    with open(filename,"r+t",encoding="utf-8") as wrtbl:
        lins_count =len(wrtbl.readlines())
        wrtbl.write(f"{lins_count+1};{name};{phone}\n")
    """
    Добавление нового пользователя
    """
    pass

def read_all(filename:str)->str:
    with open(filename,"r",encoding="utf-8") as data:
        resolt=data.read()
    return resolt
    """
    Возвращает все содержимое телефонной книги
    """
        
def search_user(data:str,filename:str)->str:
    with open(filename,"r",encoding="utf-8") as content:
        text=content.readlines()
        res=([item for item in text if data.lower() in item.lower()])
    return (''.join(res)).replace(';',' ') if res else 'Данных не найдено'
    
def copy_user(filename: str, new_filename: str, line_number: int):
    if os.path.exists(new_filename):
        mode = "a"  # Если файл существует, добавляем данные в конец
    else:
        mode = "w"  # Если файла нет, создаем новый

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if 1 <= line_number <= len(lines):
            user_data = lines[line_number - 1]
            if not duplicate_line(new_filename, user_data):
                with open(new_filename, mode, encoding="utf-8") as new_file:
                    new_file.write(user_data)
            print(f"Ошибка: Строка с номером {line_number} уже существует")
        else:
            print(f"Ошибка:Нет строки с номером {line_number} для копирования")

def duplicate_line(filename: str, user_data: str) -> bool:
    with open(filename, "r", encoding="utf-8") as file:
        return user_data in file.readlines()

def check_directory(filename:str):
    if filename not in os.listdir():
        with open(filename,"w",encoding="utf-8") as data:
            data.write("")

    

    """
    Поиск записи по критерию data
    """
   

INFO_STRING= """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - копирование
"""
DATASOURCE='phone.txt'
check_directory(DATASOURCE)
while True:
  
    mode =int(input(INFO_STRING))
    if mode==1:
        print(read_all(DATASOURCE))
    elif mode==2:
        user=input()
        phone=input()
        add_new_user(name=user,phone=phone,filename=DATASOURCE)
        pass
    elif mode==3:
        search=input('Введите данные для поиска:  ')
        print(search_user(search,DATASOURCE))
        exit()
    elif mode == 4:
        number_to_copy = int(input('Введите номер строки для копирования: '))
        copy_user(DATASOURCE, 'phone_copy.txt', number_to_copy)
