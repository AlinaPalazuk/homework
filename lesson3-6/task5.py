"""Задание 5
Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово."""

with open("./lesson3-6/file1.txt", "r") as file:
    content = file.readlines()
content2 = []
for i in content:
    i.strip()
    content2.append(i)
content = " ".join(content2)
words_list = content.lower().split(" ")
word = input("Enter the word: ")
count_of_word = 0
for i in words_list:
    if i.strip() == word:
        count_of_word += 1
print(f"Word '{word}' appears {count_of_word} times")
