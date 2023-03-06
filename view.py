import csv
def view():
    with open('file.csv', encoding='UTF-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
