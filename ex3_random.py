import csv
import random

with open('books.csv', encoding='cp1251') as file:
    books = list(csv.DictReader(file, delimiter=';'))

selected_books = random.sample(books, 20)

with open('bibliographic_references.txt', 'w', encoding='utf-8') as file:
    for i, book in enumerate(selected_books, 1):
        author = book['Автор']
        title = book['Название']
        year = book['Дата поступления'][6:][:-5] if book['Дата поступления'] else 'нет года'
        file.write(f"{i}. {author}. {title} - {year}\n")

print("Файл bibliographic_references.txt создан")