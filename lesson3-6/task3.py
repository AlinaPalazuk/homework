"""Задание 3
Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл."""

with open("./lesson3-6/file1.txt", "r") as file:
    content = file.readlines()
content.remove(content[-1])

with open("./lesson3-6/task3_result.txt", "a") as file:
    for i in content:
        file.write(f"{i}")
