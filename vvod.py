import csv
import os


def add_node():
    heading = input("Введите заголовок заметки: ")
    text_node = input("Введите текст заметки: ")

    if not os.path.exists('file.csv'):
        with open('file.csv', 'w'):
            pass

    with open('file.csv', 'r+', encoding='UTF-8', newline='') as file:
        node_id = int((len(file.readlines())) + 1)
        writer = csv.writer(file)
        writer.writerow([node_id, heading, text_node])

    file.close()
