from datetime import datetime as dt

#Добавляем время изменения/удаления/добавления контакта в файл log.txt
def add(data, operation):
    time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding = 'utf8') as file:
        file.write(f"{data}; {operation}; {time} \n")
    return