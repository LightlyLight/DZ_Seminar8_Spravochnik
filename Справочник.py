"""
Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

1
"""

# def print_contacts(file_name):
#     with open(file_name, 'r', encoding='utf8') as file:
#         all_cont = file.readlines()
#         if len(all_cont) != 0:
#             for line in all_cont:
#                 print(line.strip(), end = '\n\n')
#         else:
#             print('Список контактов пустой')

# def connect_with_user():
#     print('Введите имя, фамилию и телефон (например: Иван Иванов 89659679681): ')
#     cont_info = input()
#     return cont_info

# def add_contact(file_name):
#     with open(file_name, 'r', encoding='utf8') as file:
#         all_cont = file.readlines()
#     new_cont = connect_with_user()
#     all_cont.append('\n' + new_cont)
#     with open(file_name, 'w', encoding='utf8') as file:
#         file.writelines(all_cont)

        
# file_with_contacts = 'Contacts.txt'

# print_contacts(file_with_contacts)

def print_contacts(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            for line in all_cont:
                print(line.strip(), end='\n')
                print()
        else:
            print('Список контактов пустой')


def connect_with_user():
    print('Введите имя, фамилию и телефон (например: Иван Иванов 89659679681): ')
    cont_info = input()
    return cont_info


def add_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        new_cont = connect_with_user()
        all_cont.append('\n' + new_cont)
        with open(file_name, 'w', encoding='utf8') as file:
            file.writelines(all_cont)


def find_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()

    print("Выберите критерий для поиска:" +
    ' 1 - Имя;' +
    ' 2 - Фамилия;' +
    ' 3 - Телефон;'
    )

    comm = int(input())
    print('Введите строку для поиска:')
    data = input()
    print("Найденные контакты:")
    for cont in all_cont:
        cont_as_list = cont.strip().split()
    if data in cont_as_list[comm - 1]:
        print(*cont_as_list)

"""
Дополнить справочник возможностью копирования данных из одного файла в другой. 
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой
"""
def copy_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont_for_copy = file.readlines()
        
    copy_list_contact = []
    
    dict_contact = {}
    
    for i in range(len(all_cont_for_copy)):
        dict_contact[i] = all_cont_for_copy[i]

    for key,value in dict_contact.items(): print(key, ':', value)

    print("Выберите  номер строки c данными для копирования:")
    
    command_to_copy = int(input())
    x = dict_contact[command_to_copy] 
    print(x)

    copy_list_contact.append(x)
    new_file=open('Copy_Contacts.txt', 'w', encoding='utf8')
    for element in copy_list_contact:
        new_file.write(element)
        new_file.write('\n')
    new_file.close()



    