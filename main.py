# main.py
# FILE_NAME = 'book.txt'
import datetime
from typing import List
# import pandas as pd
def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    for line in data:
        print(line)


def save_data(file):
    print('Написать запись: ')
    dt_now = datetime.datetime.now()
    record = input('ЗАГОЛОВОК:   ')
    body = input('Тело записи:   ')
  
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{dt_now}, {record}, \n{body}\n')

def search_data(contacts: List[str]):
    
    search_str = input('поиск: ')
    founded = []
    
    for contact in contacts:
        if search_str.lower() in contact.lower():
            founded.append(contact)
    return founded

###################################
def copy_file(file):                                                           
    try:                                                                         
        with open(file, 'r', encoding='utf-8') as f:                             
            lines = f.readlines()                                                
            with open('copy_file.txt', 'w', encoding='utf-8') as cpf:            
                cpf.writelines(lines)                                            
                print('Весь файл успешно скопирован на файл (copy_file.txt)')
    except FileNotFoundError:                                                   
        print('файла нет. Сначала введите данные\n')
        return []

def copy_search(file):              
    with open('copy_search_file.txt', 'w', encoding='utf-8') as cpf:
        cpf.writelines(file)
        print('ваши данные успешно сохранены в файл (copy_search_file.txt)')

def delete_search(contacts: List[str]):
     search_str = input('поискdel: ')
     
    
     for contact in contacts:
        if search_str.lower() in contact.lower():
            print(contact)
            


def delete(fw , conta):
    
    with open(fw, 'r') as fr:
        lines = fr.readlines()
 
    with open(fw, 'w') as fw:
        for line in lines:
            if conta.lower() in line.lower():
                fw.write(line)
    print("Deleted")

        
    



               
    

def six(file):             
    file_name = file                  
    data = read_file(file_name)           
    founded_data = search_data(data)             
    show_data(founded_data)             

    flag = True              
    while flag:
        print('0 - Назад')
        print('1 - Копировать')
        print('3 - Искать заново')
        answer_copy_search = input('Выберите действие: ')
        if answer_copy_search == '0':
            flag = False
        elif answer_copy_search == '1':
            copy_search(founded_data)
        elif answer_copy_search == '3':
            data = read_file(file_name)
            founded_data = delete_search(data)
            show_data(founded_data)

def foor(file):             
    file_name = file                  
    data = read_file(file_name)           
    founded_data = delete_search(data)             
    # show_data(found4
    # ed_data)             

    flag = True              
    while flag:
        print('0 - Назад')
        print('1 - удалить')
        print('3 - Искать заново')
        answer_copy_search = input('Выберите действие: ')
        if answer_copy_search == '0':
            flag = False
        elif answer_copy_search == '1':
            delete(file, founded_data)
        elif answer_copy_search == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)

def main():
    file_name = 'book.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - найти и удалить запись ')
        print('5 - копировать все данные')
        print('6 - найти и копировать определенные данные')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':                
            foor(file_name)  

        elif answer == '5':
            # data = read_file(file_name) 
            # copy_file(data)              
            copy_file(file_name)          

        elif answer == '6':
            six(file_name)               



if __name__ == '__main__':
    main()