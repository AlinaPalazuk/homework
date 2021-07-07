"""Задание 2
Дан текстовый файл. Необходимо создать новый файл и записать в него следующую 
статистику по исходному файлу:
■ Количество символов;
 ■ Количество строк;
 ■ Количество гласных букв;
 ■ Количество согласных букв; 
 ■ Количество цифр."""

s = open("./lesson3-6/file2.txt", mode = "r")
lines = s.readlines()
count_strings = len(lines)
s.close()
s = open("./lesson3-6/file2.txt", mode = "r")
content = s.read()
s.close()
count_symbols = len(content)
def string_statistic(string, base_list):
    count = 0
    for i in string:
        if i in base_list:
            count += 1
    return count
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
vowels = ['a', 'e', 'i', 'o', 'u', 'y',]
consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 
    'q', 'r', 's', 't', 'v', 'w', 'x', 'z',
    ]
count_numbers = string_statistic(content, numbers)
count_vowels = string_statistic(content, vowels)
count_consonants = string_statistic(content, consonants)

w = open("./lesson3-6/text_statistic.txt", mode = "w")
w.write(
    f"TEXT STATISTIC\nCount of strings: {count_strings},\nCount of symbols: {count_symbols},\nCount of vowel: {count_vowels},\nCount of consonants: {count_consonants},\nCount of numbers: {count_numbers}"
    )

w.close()
