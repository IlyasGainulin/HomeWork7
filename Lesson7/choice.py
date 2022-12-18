import csv
import os
from os import system
from show import export_directory
from add_contact import add_contacts_from_phonebook, add_contact_from_keyboard
from add_phonebook import add_new_directory, import_new_dir_at_directory
from show import display_directory_screen

def method_selection(num): # Выбор метода
    if num == 1:
        system("cls")
        add_new_directory('telephone.csv')
        user_interface()
        exit()
    elif num == 2:
        os.system('dir')
        user_interface()
        exit()
    elif num == 3:
        system("cls")
        display_directory_screen('telephone.csv')
        print('')
        user_interface()
        exit()
    elif num == 4:
        system("cls")
        file_csv_new = input('Введите файл *.csv > ')
        import_new_dir_at_directory(file_csv_new, 'telephone.csv')
        user_interface()
        exit()
    elif num == 5:
        system("cls")
        file_txt = input('Введите файл *.txt > ')
        add_contacts_from_phonebook(file_txt)
        user_interface()
        exit()
    elif num == 6:
        add_contact_from_keyboard()
        user_interface()
        exit()
    elif num == 7:
        system("cls")
        file_txt = input('Введите файл *.txt > ')
        export_directory(file_txt)
        user_interface()
        exit()
    elif num == 8:
        exit()

def user_interface(): # Меню
    print('Список возможностей в телефонном справочнике! \n Выберите один из пунктов:')
    print('1. Создать новый телефонный справочник (telephone.csv)')
    print('2. Вывести список файлов в папке на экран ')
    print('3. Вывести основной телефонный справочник на экран')
    print('4. Импортировать справочник из csv файла')
    print('5. Импортировать справочник из txt файла')
    print('6. Ввести новый контакт с клавиатуры ')
    print('7. Экспортировать основной справочник в txt файл')
    print('8. Выход \n')
    num = input('Введите число от 1 до 8 > ')
    try:
        num = int(num)
    except:
        system("cls")
        print('Это не число')
        user_interface()
        exit()
    if 1 <= int(num) <= 8:
        method_selection(num)
    else:
        system("cls")
        print('Неправильное число')
        user_interface()
        exit()