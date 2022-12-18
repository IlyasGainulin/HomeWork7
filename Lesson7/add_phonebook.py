import csv
from add_contact import read_last_id

def add_new_directory(file_csv): # Добавление нового справочника
    with open(file_csv, 'w', newline='') as csvfile:
        fieldnames = ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'id': '1', 'First_Name': 'Тихон', 
            'Last_Name': 'Панфилов', 'Number': '84956063430', 'Description': 'Бездельник'})
        writer.writerow({'id': '2', 'First_Name': 'Ульяна', 
            'Last_Name': 'Краснова', 'Number': '84952986918', 'Description': 'Начальник отдела'})
        writer.writerow({'id': '3', 'First_Name': 'Марк', 
            'Last_Name': 'Рогов', 'Number': '84951659021', 'Description': 'Директор'})

def import_new_dir_at_directory(file_csv_new, file_csv): # Импортирование нового справочника(csv файл) в основной справочник
    last_id = read_last_id() + 1
    with open(file_csv_new, newline='') as csvfile_in:
        reader = csv.DictReader(csvfile_in)
        with open(file_csv, 'a', newline='') as csvfile_out:
            fieldnames = ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            for row in reader:
                writer.writerow({'id': last_id, 'First_Name': row['First_Name'], 
                    'Last_Name': row['Last_Name'], 'Number': row['Number'], 
                    'Description': row['Description']})
                last_id = last_id + 1