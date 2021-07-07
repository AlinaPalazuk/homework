"""Задание 4
Дан текстовый файл. Найти длину самой длинной строки."""

with open("./lesson3-6/file1.txt", "r") as file:
    content = file.readlines()
for i in content:
    max_length = 0
    if len(i) > max_length:
        max_length = len(i)
print(max_length)
