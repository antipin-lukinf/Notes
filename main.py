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

    with open('file.csv', 'r+', encoding='UTF-8', newline='') as file:
        node_id = int((len(file.readlines()))+1)
        writer = csv.writer(file)
        writer.writerow([node_id, heading, text_node])

    file.close()

while True:
    print("1 - Новая заметка")
    print("2 - Напечатать все заметки")
    print("3 - удалить заметку по id")
    print("6 - Закрытие программы")

    option = int(input("Выберите действие: "))
    if option == 1:
        new_node()

    elif option == 2:
        with open('file.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    elif option == 3:
        del_str = input("Введите id заметки, которую хотите удалить: ")
        with open('file.csv', 'r') as inp, open('file_out.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                id = row[0]
                if id != del_str:
                    writer.writerow(row)
        os.remove('file.csv')
        os.renames("file_out.csv", "file.csv")


    elif option == 6:
        print("See you")
        exit(6)
    else:
        print("Введены не корректные данные")

