import re


text = """
Вчера программист Ivan решил переписать старый код. В исходниках он нашел странные пометки от прошлого разработчика, которые выглядели как случайный набор букв: просто a, затем ab, чуть дальше abb и даже длинное abbb. В одной из строк прятался странный пароль, который начинался на 'a', содержал всякий мусор и заканчивался на 'b', например: a_super_secret_hash_blob.

В базе данных хранились переменные в разных форматах. Там были идентификаторы вроде user_id, first_name и dark_theme_enabled. Однако новый стандарт требовал использовать другой стиль, поэтому Ivan переделал их в userId, firstName и darkThemeEnabled.

Логи системы, которые ему прислали, выглядели неряшливо: "Ошибка, сбой сети. Перезагрузка системы." — здесь нужно было заменить все знаки препинания и пробелы на двоеточия.

Для красивого вывода на экран ему также пришлось поработать с именами классов. У него были строки вроде ParseTextData и GenerateNewReport. Ему нужно было написать скрипт, чтобы разбить эти строки на отдельные слова, а затем вставить между ними пробелы. В конце дня он так устал, что захотел написать функцию, которая возьмет myCamelCaseText и превратит его обратно в my_camel_case_text.

"""

# Write a Python program that
# matches a string that has an 'a' followed by zero or more 'b''s.

first = re.findall(r"ab*", text)

# Write a Python program that matches a
# string that has an 'a' followed by two to three 'b'.

second = re.findall(r"ab{2,3}", text)

# Write a Python program to
# find sequences of lowercase letters joined with a underscore.

third = re.findall(r"[a-z]+_[a-z]+", text)

# Write a Python program to find the
# sequences of one upper case letter followed by lower case letters.
a4 = re.findall(r"\b[A-Z][a-z]+\b", text)

# Write a Python program that matches a string
# that has an 'a' followed by anything, ending in 'b'.
a5 = re.fullmatch(r"^a.*b$", text)

# Write a Python program to replace
# all occurrences of space, comma, or dot with a colon.

a6 = re.sub(r"[ ,.]", "|", text)

# Write a python program to convert
# snake case string to camel case string user_id в userId
a7 = re.sub(r"_([a-z])", lambda match: match.group(1).upper(), text)


# Write a Python program to split a string at uppercase letters.

a8 = re.split(r"(?=[A-Z])", text)
print([x for x in a8 if x])

# Write a Python program to insert
# spaces between words starting with capital letters.

a9 = re.sub(r"(?=[A-Z])", " ", text).strip()

# Write a Python program to convert a
# given camel case string to snake case.

a10 = re.sub(r"([a-z])([A-Z])", r"\1_\2", text).lower()