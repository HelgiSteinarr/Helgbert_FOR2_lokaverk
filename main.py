import csv


with open ("sheeptest.txt", "r", encoding="utf-8") as file:
    data = csv.reader(file, delimiter=";")
    for i in data:
        print(i[4])