from Справочник import *

CONTACTS = 'Contacts.txt'

# def interface():
#     while True:
#         print('Выберете действие:\
#         \n 1 - Добавить контакт \
#         \n 2 - Вывести все контакты \
#         \n 0 - Выйти')
#         command = int(input())
#         match command:
#             case 0:
#                 break
#             case 1:
#                 add_contact(CONTACTS)
#             case 2:
#                 print_contacts(CONTACTS)

# if __name__ == '__main__':
#     interface()

def interface():
    while True:
        print('Выберете действие:\n' +
        '1 - Добавить контакт\n' +
        '2 - Вывести все контакты\n' +
        '3 - Найти контакт\n' +
        '4 - Скопировать контакт\n' +
        '0 - Выйти')
        print()
        command = int(input())
        match command:
            case 0:
                break
            case 1:
                add_contact(CONTACTS)
            case 2:
                print_contacts(CONTACTS)
            case 3:
                find_contact(CONTACTS)
            case 4:
                copy_contact(CONTACTS)
            case _:
                print("Не верная команда!")


if __name__ == '__main__':
    interface()


