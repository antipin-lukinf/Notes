import csv
import os
import pandas as pd

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

    # df = pd.read_csv('file.csv', header=None)
    # df.rename(columns={0: 'node_id', 1: 'heading', 2: 'text_node'}, inplace=True)
    # df.to_csv('file.csv', index=False)  # save to new csv file

    file.close()

while True:
    print("1 - Новая заметка")
    print("2 - Напечатать все заметки")
    print("3 - удалить заметку по id")
    print("4 - редактировать заметку по id")
    print("6 - Закрытие программы")

    option = int(input("Выберите действие: "))
    if option == 1:
        new_node()

    elif option == 2:
        with open('file.csv', encoding='UTF-8',  newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

    elif option == 3:
        del_str = input("Введите id заметки, которую хотите удалить: ")
        with open('file.csv', 'r', encoding='UTF-8', newline='') as inp, open('file_out.csv', 'w', encoding='UTF-8', newline='') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                id = row[0]
                if id == del_str:
                    del_str_int = int(del_str)
                    print(del_str_int)
                    row[del_str_int] = 'none'
                    row[del_str_int + 1] = 'none'
                writer.writerow(row)
                # if id != del_str:
                #     writer.writerow(row)
        os.remove('file.csv')
        os.renames("file_out.csv", "file.csv")

    elif option == 4:
        insert_str = input("Введите id заметки, которую хотите отредактировать: ")
        with open('file.csv', 'r', encoding='UTF-8', newline='') as inp, open('file_out.csv', 'w', encoding='UTF-8', newline='') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                id = row[0]
                if id == insert_str:
                    insert_str_int = int(insert_str)
                    row[insert_str_int] = input('Введите новый заголовок заметки: ')
                    row[insert_str_int+1] = input('Введите новый текст заметки: ')
                writer.writerow(row)

        os.remove('file.csv')
        os.renames("file_out.csv", "file.csv")


    elif option == 6:
        print("See you")
        exit(6)
    else:
        print("Введены не корректные данные")

