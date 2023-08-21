import interface
import database_module
import logger
import import_from_file as iff
import export_to_file


def run():
    
    while True:
    
        command = interface.start_page()

        match command:
            case '1':     # Список всех контактов
                data = database_module.get_all_contacts()
                interface.show_contacts(data)

            case '2': # Поиск контакта
                user_search = interface.search_contact()
                data = database_module.get_contact_info(user_search)
                interface.show_contacts(data)
            
            
            case '3': # Добавить контакт

                new_contact = interface.add_contact()
                database_module.add_contacts(new_contact)
                logger.add(new_contact, 'added')
                interface.done_message()

            case '4': # Изменить дело
                data = database_module.get_all_contacts()
                interface.show_contacts(data)
                deal_id = interface.change_contact()
                one_contact = database_module.get_one_contact(deal_id)
                changed_contact = interface.change_contact_content(one_contact)
                if changed_contact['comment'] == 'Я что-то нажал и всё сломалось':
                    database_module.delete_contact(changed_contact['contact_id'])
                    logger.add(changed_contact, 'deleted')
                else:
                    database_module.change_contact(changed_contact)
                    logger.add(changed_contact, 'changed')
            
            case '5': # Импорт
                user_choice = interface.import_contacts()
                if user_choice == 'csv':
                    data = iff.import_csv('import_phonebook.csv')
                    database_module.add_contacts(data)
                    interface.result_mess(True)
                    logger.add(data, 'imported')
                elif user_choice == 'json':
                    data = iff.import_json('import_phonebook.json')
                    database_module.add_contacts(data)
                    interface.result_mess(True)
                    logger.add(data, 'imported')
                else:
                    interface.error_input()
                
                
            
            case '6': # Экспорт
                export_to_file.export_csv()
                # user_choice = interface.export_contacts()
                # if user_choice == 'csv':
                #     data = export_to_file.export_csv()

                #     interface.result_mess(True)
                #     #logger.add(data, 'exported')
                # elif user_choice == 'json':
                #     #data = export_to_file.export_json()
                    
                #     interface.result_mess(False)
                #     #logger.add(data, 'exported')
                # else:
                #     interface.error_input()

            case '7': # Выход
                interface.bye_mess()
                break
            
            case _:
                interface.error_input()


def change_action(user_answer: dict):
    match user_answer['user_choise']:
        case 1: # завершить дело
            return
        
        case 2: # изменить дело
            return

        case 3: # удалить дело
            return
