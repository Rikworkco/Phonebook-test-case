import csv
import json

# test_imported_data = [{'contact_id': '' ,'surname': 'Иванов', 'name': 'Иван', 'phone': '111', 'comment': 'Друг'}, 
#                     {'contact_id': '' ,'surname': 'Петров', 'name': 'Петр', 'phone': '222', 'comment': 'Коллега'},
#                     {'contact_id': '' ,'surname': 'Сидоров', 'name': 'Сидор', 'phone': '333', 'comment': 'Должен 1000'},
#                     {'contact_id': '' ,'surname': 'Ромашкина', 'name': 'Маша', 'phone': '444', 'comment': 'Вкусные пирожки'},
#                     {'contact_id': '' ,'surname': 'Василькова', 'name': 'Оля', 'phone': '555', 'comment': 'Большие глаза'}]

def import_csv(path_to_import_csv_file): 
    data = [] # Список словарей который получим при преобразовании       
    with open(path_to_import_csv_file, "r", newline='', encoding='UTF-8-sig') as file: 
        file_reader = csv.DictReader(file, delimiter = ";") 
        for row in file_reader:
            #row['contact_id'] = '' # Добавляем пустой ключ contact_id в словарь
            data.append(row)     
        for i in range(0, len(data)): 
            d1 = {'contact_id': ''}
            data[i], d1 = d1, data[i]
            data[i].update(d1)     

    return data 
    
def import_json(path_to_import_json_file):
    data = [] # Список словарей который получим при преобразовании      
    with open(path_to_import_json_file, 'r', encoding='UTF-8') as file: #Открываем файл на чтение
        data = json.load(file) #загружаем из файла данные в словарь data
        for i in range(0, len(data)): 
            d1 = {'contact_id': ''}
            data[i], d1 = d1, data[i]
            data[i].update(d1)
    return data


# Выбираем формат файла импортируемых контактов
# def choice_format():
#     print('Телефонную книгу в каком формате изволите импотировать? \n.txt - 1 .csv - 2 .json - 3:')
#     choice = int((input()))
#     match choice:
#        # case 1: return import_txt()
#         case 2: return import_csv(path_to_import_csv_file)
#         case 3: return import_json(path_to_import_json_file)
#         case _ :
#             print('Неизвестный формат файла')
#             exit()

if __name__ == "__main__":
    from pprint import pprint
    path_to_import_json_file = 'import_phonebook.json'
    path_to_import_csv_file = 'import_phonebook.csv'
    #pprint(choice_format(), sort_dicts=False)
    # pprint('******************test_imported_data******************')
    # pprint(test_imported_data, sort_dicts=False)
    
    pprint('******************csv_file******************')
    pprint(import_csv(path_to_import_csv_file), sort_dicts=False)
    
    pprint('******************json_file******************')
    pprint(import_json(path_to_import_json_file), sort_dicts=False)



  
