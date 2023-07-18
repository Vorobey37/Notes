
import datetime
import json



def add(note):

    id = 1
    head = input("\n""Введите заголовок заметки: ""\n")
    body = input("\n""Введите тело заметки: ""\n")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    text = list()

    while True:
        if id in note:
            id += 1
        else:
            note[id] = text
            text.append(id)
            text.append(time)
            text.append(head)
            text.append(body)
            break



def read(note):

    while True:
        menu_number = input("\n""Какие заметки вывести?""\n"
                        "1 - вывести весь список" "\n"
                        "2 - выбрать дату добавления/изменения заметки" "\n" )
        
        if menu_number == "1":
            for i in note:
                print()
                for j in range(len(note[i])):
                    print(note[i][j])
            break

        if menu_number == "2":
            date_element = input("\n""Введите дату в формате ГГГГ-ММ-ДД:""\n")

            for i in note:
                if date_element in note[i][1]:
                    print()
                    for j in range(len(note[i])):
                        print(note[i][j])

                else:
                    print("\n""По указанной дате нет заметок...")
                    break
            break    

        print("\n""Такой команды нет! Еще раз: ") 



def redact(note):

    redact_element = input("\n""Введите параметр для поиска: ""\n")
    count = 0

    for i in note:    
        for j in range(1, len(note[i])):
            if redact_element in note[i][j]:
                count += 1
                print("\n""Найдена заметка:")
                print(note[i])

                while True:
                    menu_number = input("1 - редактируем заметку""\n"
                                   "2 - оставляем как есть""\n")                   
                    if menu_number == "1" or menu_number == "2":
                        break
                    print("\n""Нет такой команды, выберите 1 или 2:")

                if menu_number == "1":
                    head = input("\n""Введите заголовок заметки: ""\n")
                    body = input("\n""Введите тело заметки: ""\n")
                    time = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
                    text = list()
                    text.append(i)
                    text.append(time)
                    text.append(head)
                    text.append(body)
                    note[i] = text
                    break

                if menu_number == "2":
                    pass

    if count == 0:
        print("Не нашлось ни одной записи...")

    print(note) 



def delete(note):

    delete_element = input("Введите параметр для поиска: ""\n")
    count = 0
    list_to_delete = list() 
     
    for i in note:    
        for j in range(1, len(note[i])):          
            if delete_element in note[i][j]:
                count += 1
                print("Найдена заметка:")
                print(note[i])

                while True:
                    menu_number = input("1 - удаляем заметку""\n"
                                   "2 - оставляем как есть""\n")
                    if menu_number == "1" or menu_number == "2":
                        break
                    print("\n""Нет такой команды, выберите 1 или 2:""\n")

                if menu_number == "1":
                    list_to_delete.append(i)
                    break

                if menu_number == "2":
                    pass

    if count == 0:
        print("Не нашлось ни одной записи...")

    for i in list_to_delete:
        del note[i]

    print(note) 



def can_exit(flag):

    while True:
            exit_menu = input("\n""Продолжить работу с приложением: (y/n)?""\n")            
            if exit_menu.lower() == "y":
                return flag
            
            if exit_menu.lower() == "n":
                flag = False
                return flag
                       
            print("Такой команды нет! Еще раз: ")



def parse(note):

    note_values = list()
    note_keys = list()

    for i in note:
        note_values.append(note[i])
        note_keys.append(int(note[i][0]))

    note = {}

    for i in range(len(note_keys)):
        note[note_keys[i]] = note_values[i]

    return note


# Поехали!
try:
    with open('NoteBook.txt', 'r', encoding = 'utf-8') as json_file:
        note = json.load(json_file)
except:
    with open('NoteBook.txt', 'w', encoding = 'utf-8') as json_file:
        note = {}
        json.dump(note, json_file)

note = parse(note)
flag = True

while flag:   
    print("\n""Введите номер команды:" "\n"
        "1 - создать заметку" "\n"
        "2 - читать заметки" "\n"
        "3 - редактировать заметки" "\n"
        "4 - удалить заметки" "\n"
        "5 - выход из приложения" "\n")    
    number_menu = input()

    if number_menu == "1":
        add(note)
        print(note)
        flag = can_exit(flag)        
        continue

    if number_menu == "2":
        read(note)
        flag = can_exit(flag)
        continue

    if number_menu == "3":
        redact(note)
        flag = can_exit(flag)
        continue

    if number_menu == "4":
        delete(note)
        flag = can_exit(flag)
        continue

    if number_menu == "5":
        break

    print("Команда неверная, попробуйте еще раз: ")

with open('NoteBook.txt', 'w', encoding = 'utf-8') as json_file:
    json.dump(note, json_file)
