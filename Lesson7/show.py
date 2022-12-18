import csv

def display_directory_screen(file_csv): # Вывод справочника на экран
    with open(file_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['id'], row['First_Name'], row['Last_Name'], row['Number'], row['Description'])
            
def export_directory(file_txt):#Экспорт справочника из txt файла
    with open('telephone.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            with open(file_txt, 'a') as txtfile:
                stroka = ''
                stroka = str(row)
                txtfile.write(f'{stroka} \n')

def read_last_id(): # Считывание последнего ID
    with open('telephone.csv', newline='') as csvfile:
        last_line = csvfile.readlines()[-1]
        last_line = last_line[0].split(',')
        last_id = int(last_line[0])
        return last_id