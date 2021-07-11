"""Задание 6
Дан текстовый файл. Найти и заменить в нем заданное слово. 
Что искать и на что заменять определяется пользователем."""

with open("./lesson3-6/file1.txt", "r") as file:
    content = file.read()

content = content.replace(input("Find word: "), input("Replace with: "))

with open("./lesson3-6/file1_replace.txt", "w") as file:
    file.writelines(content)