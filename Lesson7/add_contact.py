import csv
from show import read_last_id

def add_new_contact(new_contact): # Добавление нового контакта не из csv
    last_id = read_last_id() + 1
    with open('telephone.csv', 'a', newline='') as csvfile_out:
            fieldnames = ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            writer.writerow({'id': last_id, 'First_Name': new_contact[0], 
                'Last_Name': new_contact[1], 'Number': new_contact[2], 
                'Description': new_contact[3]})

def add_contacts_from_phonebook(file_txt): # Добавление контактов из txt файла
    with open(file_txt, 'r') as file:
        count = 0
        new_contact = []
        lines = file.readlines()
        for line in lines:
            if line.strip() == '':
                count = count
            else:
                new_contact.append(line.strip())
                count = count + 1          
            if count == 4:
                add_new_contact(new_contact)
                count = 0
                new_contact = []
            else:
                continue

def add_contact_from_keyboard(): # Вызов метода набора контакта с клавиатуры
    print('С клавиатуры Имя/Фамилия/Номер/Описание')
    new_contact = []
    for i in range(4):
        new_contact.append(str(input()))
    add_new_contact(new_contact)