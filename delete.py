import os
import csv


def delete():
    del_str = input("Введите id заметки, которую хотите удалить : ")
    with open('file.csv', 'r', encoding='UTF-8', newline='') as inp, open('file_out.csv', 'w', encoding='UTF-8',
                                                                          newline='') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            id = row[0]
            if id == del_str:
                del_str_int = int(del_str)
                print(del_str_int)
                row[del_str_int] = 'none'
                row[del_str_int + 1] = 'none'
            writer.writerow(row)

    os.remove('file.csv')
    os.renames("file_out.csv", "file.csv")