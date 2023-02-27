import csv
import os

def new_node():

    add_node()

def add_node():

    heading = input("Введите заголовок заметки: ")
    text_node = input("Введите текст заметки: ")

    if not os.path.exists('file.csv'):
        with open('file.csv', 'w'):
            pass

    with open('file.csv', 'r+') as file:
        node_id = int((len(file.readlines()))/2)
        print(node_id)

        writer = csv.writer(file)
        writer.writerow([node_id, heading, text_node])

    file.close()

while True:
    print("1 - Новая заметка")
    print("2 - Закрытие программы")

    option = int(input("Выберите действие: "))
    if option == 1:
        new_node()
    elif option == 2:
        print("See you")
        exit(2)
    else:
        print("Введены не корректные данные")

