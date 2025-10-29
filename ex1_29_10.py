import csv

with open('books.csv', encoding='cp1251') as file:
    books = list(csv.DictReader(file, delimiter=';'))

name = 'Название'

count = sum(len(r[name]) > 30 for r in books)
print("Ответ:", count)