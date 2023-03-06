import csv
import os

import view
import delete
import vvod
import redact


while True:
    print("1 - Новая заметка")
    print("2 - Напечатать все заметки")
    print("3 - удалить заметку по id")
    print("4 - редактировать заметку по id")
    print("6 - Закрытие программы")

    option = int(input("Выберите действие: "))
    if option == 1:
        vvod.add_node()

    elif option == 2:
        view.view()


    elif option == 3:
        delete.delete()


    elif option == 4:
        redact.red()



    elif option == 6:
        print("See you")
        exit(6)
    else:
        print("Введены не корректные данные")

