
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
        menuRead = input("\n""Какие заметки вывести?""\n"
                        "1 - вывести весь список" "\n"
                        "2 - выбрать дату добавления/изменения заметки" "\n" )
        if menuRead == "1":
            for i in note:
                print()
                print(note[i][0])
                print(note[i][1])
                print(note[i][2])
                print(note[i][3])
                print()
            break
        if menuRead == "2":
            dateElement = input("\n""Введите дату в формате ГГГГ-ММ-ДД:""\n")
            for i in note:
                if dateElement in note[i][1]:
                    print()
                    print(note[i][0])
                    print(note[i][1])
                    print(note[i][2])
                    print(note[i][3])
                    print()
                else:
                    print("\n""По указанной дате нет заметок...")
                    break
            break                   
        print("\n""Такой команды нет! Еще раз: ")    

def redact(note):
    element = input("\n""Введите параметр для поиска: ""\n")
    count = 0
    for i in note:    
        for j in range(1, len(note[i])):
            if element in note[i][j]:
                count += 1
                print("\n""Найдена заметка:")
                print(note[i])
                while True:
                    number = input("1 - редактируем заметку""\n"
                                   "2 - оставляем как есть""\n")
                    if number == "1" or number == "2":
                        break
                    print("\n""Нет такой команды, выберите 1 или 2:")
                if number == "1":
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
                if number == "2":
                    pass
    if count == 0:
        print("Не нашлось ни одной записи...")
    print(note)   

def delete(note):
    element = input("Введите параметр для поиска: ""\n")
    count = 0
    listToDelete = list() 
     
    for i in note:    
        for j in range(1, len(note[i])):
            if element in note[i][j]:
                count += 1
                print("Найдена заметка:")
                print(note[i])
                while True:
                    number = input("1 - удаляем заметку""\n"
                                   "2 - оставляем как есть""\n")
                    if number == "1" or number == "2":
                        break
                    print("\n""Нет такой команды, выберите 1 или 2:""\n")
                if number == "1":
                    listToDelete.append(i)
                    break
                if number == "2":
                    pass
    if count == 0:
        print("Не нашлось ни одной записи...")
    for i in listToDelete:
        del note[i]
    print(note) 

def askForExit(flag):
    while True:
            menuExit = input("\n""Продолжить работу с приложением: (y/n)?""\n")
            if menuExit.lower() == "y":
                return flag
            if menuExit.lower() == "n":
                flag = False
                return flag           
            print("Такой команды нет! Еще раз: ")

def parseNote(note):
    noteValues = list()
    noteKeys = list()
    for i in note:
        noteValues.append(note[i])
        noteKeys.append(int(note[i][0]))
    note = {}
    for i in range(len(noteKeys)):
        note[noteKeys[i]] = noteValues[i]
    return note


# Поехали!
try:
    with open('NoteBook.txt', 'r', encoding = 'utf-8') as jsonFile:
        note = json.load(jsonFile)
except:
    with open('NoteBook.txt', 'w', encoding = 'utf-8') as jsonFile:
        note = {}
        json.dump(note, jsonFile)
note = parseNote(note)
flag = True
while flag:   
    print("\n""Введите номер команды:" "\n"
        "1 - создать заметку" "\n"
        "2 - читать заметки" "\n"
        "3 - редактировать заметки" "\n"
        "4 - удалить заметки" "\n"
        "5 - выход из приложения" "\n")    
    menuNumber = input()
    if menuNumber == "1":
        add(note)
        print(note)
        flag = askForExit(flag)        
        continue       
    if menuNumber == "2":
        read(note)
        flag = askForExit(flag)
        continue
    if menuNumber == "3":
        redact(note)
        flag = askForExit(flag)
        continue
    if menuNumber == "4":
        delete(note)
        flag = askForExit(flag)
        continue
    if menuNumber == "5":
        break
    print("Команда неверная, попробуйте еще раз: ")
with open('NoteBook.txt', 'w', encoding = 'utf-8') as jsonFile:
    json.dump(note, jsonFile)
