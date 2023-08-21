# Работа с базой данных

import json

path_to_db = 'db_phonebook.json'

def get_all_contacts():  # Возвращаем весь список контактов из файла db_phonebook.json
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        data = [data[i] for i in range(0, len(data))]
    return data

def get_one_contact(contact_id_get): # Возвращаем один контакт через contact_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        one_contact_get = {}
        for i in range(0, len(data)): 
            if contact_id_get == data[i]['contact_id']:
                one_contact_get = data[i]
                break
    return one_contact_get

def get_contact_info(contact_info_get): # Возвращаем контакты по вхождению в значение любого из ключей surname, name, phone, comment
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        info_contact_get = []

        for i in range(0, len(data)): 
            if  contact_info_get.lower() in data[i]['surname'].lower():
                info_contact_get.append(data[i])
            elif contact_info_get.lower() in data[i]['name'].lower():
                info_contact_get.append(data[i])
            elif contact_info_get.lower() in data[i]['phone'].lower():
                info_contact_get.append(data[i])
            elif contact_info_get.lower() in data[i]['comment'].lower():
                info_contact_get.append(data[i])
 
    return info_contact_get

def add_contacts(contacts_new_dict):  # Добавление новых контактов в БД [{'contact_id': '', 'surname': 'Петров', 'name': 'Иван', 'phone': '111', 'comment': 'Друг'}, 
                                                                        #{'contact_id': '', 'surname': 'Васильков', 'name': 'Иван', 'phone': '111', 'comment': 'Друг'}]
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)            
        for i in range(0, len(contacts_new_dict)): 
            contacts_new_dict[i]['contact_id'] = data[len(data)-1]['contact_id'] + 1
            data.append(contacts_new_dict[i])     # Добавляем в список словарей новый контакт   
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)

def change_contact(contact_edit):  # Изменяем контакт
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)

        for i in range(0, len(data)): # Чтобы изменить контакт c conroct_id = 6, находим в БД словарь с contact_id = 6 и перезаписываем его.
            if contact_edit['contact_id'] == data[i]['contact_id']:
                data[i] = contact_edit
        
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)    

def delete_contact(contact_id_delete): # Удаляем контакт в БД по его contact_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
                  
        for i in range(0, len(data)): 
            if data[i]['contact_id'] == contact_id_delete: # Находим индекс элемента в списке словарей с нужным deal_id
                index_del = i
                break
        data.pop(index_del)   # Удаляем из списка словарь с нужным contact_id
        for i in range(0, len(data)): # Перезаписаваем в каждом словаре списка ключ contact_id
            data[i]['contact_id'] = i+1
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)    

def clear_db(path_to_db): # Очищаем базу данных
    first_element = [{'id_counter': 0}, ]
    with open(path_to_db, 'w') as file:
        json.dump(first_element, file, indent=4)

if __name__ == "__main__":
#Тестирование БД на тестовых данных test_data
    from pprint import pprint
    
    path_to_db = 'test_db_phonebook.json'
    
    clear_db(path_to_db)
    test_data =[{'contact_id': 1, 'surname': 'Иванов', 'name': 'Иван', 'phone': '111', 'comment': 'Друг'}, 
                {'contact_id': 2, 'surname': 'Петров', 'name': 'Петр', 'phone': '222', 'comment': 'Коллега'},
                {'contact_id': 3, 'surname': 'Сидоров', 'name': 'Сидор', 'phone': '333', 'comment': 'Должен 1000'},
                {'contact_id': 4, 'surname': 'Ромашкина', 'name': 'Маша', 'phone': '444', 'comment': 'Вкусные пирожки'},
                {'contact_id': 5, 'surname': 'Василькова', 'name': 'Оля', 'phone': '555', 'comment': 'Большие глаза'}]
    

    with open (path_to_db, 'w') as test_file:
        json.dump(test_data,test_file, indent=4)

    print('')
    print('***get_all_contacts()***')
    pprint(get_all_contacts(), sort_dicts=False)

    print('')
    print('***add_contact(test_contact_add)***')
    test_contacts_add = [{'contact_id': '', 'surname': 'Петров', 'name': 'Иван', 'phone': '111', 'comment': 'Друг'}, 
                        {'contact_id': '', 'surname': 'Васильков', 'name': 'Иван', 'phone': '111', 'comment': 'Друг'}]
    print('*' * 10)
    print(test_contacts_add)    
    print('*' * 10)    
    add_contacts(test_contacts_add)
    with open (path_to_db, 'r') as test_file:
        text = json.load(test_file)
        pprint(text, sort_dicts=False)

    print('')
    print('***change_contact(test_contact_edit)***')
    test_contact_edit = {'contact_id': 3, 'surname': 'Сидоров', 'name': 'Сидор', 'phone': '333', 'comment': 'Должен 7777000'}
    change_contact(test_contact_edit)
    with open (path_to_db, 'r') as test_file:
        text = json.load(test_file)
        pprint(text, sort_dicts=False)

    print('')
    print('***get_one_contact(test_contact_id_get)***')
    test_contact_id_get = 3
    print(get_one_contact(test_contact_id_get))

    print('')
    print('***delete_contact(contact_delete)***')
    test_contact_id_delete = 5
    print('*' * 10) 
    print(get_one_contact(test_contact_id_delete))
    print('*' * 10) 
    delete_contact(test_contact_id_delete)
    with open (path_to_db, 'r') as test_file:
        text = json.load(test_file)
        pprint(text, sort_dicts=False)
        
    print('')
    print('***get_contact_info(contact_info_get)***')
    print('*' * 10) 
    contact_info_get = 'дол'
    print(contact_info_get)
    print('*' * 10) 
    pprint(get_contact_info(contact_info_get), sort_dicts=False)