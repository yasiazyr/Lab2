import csv

with open('books.csv', encoding='cp1251') as file:
    books = list(csv.DictReader(file, delimiter = ';'))

name = 'Название'
author = 'Автор'
date = 'Дата поступления'

author_name = input("Какой автор Вас интересует?")
author_list = []
for r in books:
    year = int(r[date][6:][:-5])
    if author_name in str(r[author]) and (year == 2015 or year == 2018):
        author_list.append(r)

if len(author_list)==0:
    print('Такого автора нет')

for s in author_list:
    print(s[author], s[name], s[date][:-5])

