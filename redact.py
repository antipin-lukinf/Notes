import csv
import os


def red():
    insert_str = input("Введите id заметки, которую хотите отредактировать: ")
    with open('file.csv', 'r', encoding='UTF-8', newline='') as inp, open('file_out.csv', 'w', encoding='UTF-8',
                                                                          newline='') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            id = row[0]
            if id == insert_str:
                insert_str_int = int(insert_str)
                row[insert_str_int] = input('Введите новый заголовок заметки: ')
                row[insert_str_int + 1] = input('Введите новый текст заметки: ')
            writer.writerow(row)

    os.remove('file.csv')
    os.renames("file_out.csv", "file.csv")