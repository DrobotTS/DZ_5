# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
# Это одно задание. При выполнении пунктов можно использовать объекты полученные в предыдущих пунктах.

persons = [
    {"name": "Ronda", "age": 17},
    {"name": "Dan", "age": 12},
    {"name": "Davidson", "age": 5},
    {"name": "Gru", "age": 3},
    {"name": "Kevin", "age": 3},
    {"name": "Piterson", "age": 55}
]

youngest_persons = []

young = 150

for person in persons:
    if person["age"] < young:
        youngest_persons.clear()
        youngest_persons.append(person["name"])
        young = person["age"]
    elif young == person["age"]:
        youngest_persons.append(person["name"])

print(f"Print youngest persons: {youngest_persons}")

longest_name = []
min_long = 0

for person in persons:
    if len(person["name"]) > min_long:
        longest_name.clear()
        longest_name.append(person["name"])
        min_long = len(person["name"])
    elif min_long == len(person["name"]):
        longest_name.append(person["name"])

print(f"Print longest name: {longest_name}")

ages = []
for person in persons:
    age = person["age"]
    ages.append(age)

avarage_age = sum(ages) // len(ages)
print(f"Print avarage age: {avarage_age}")

# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.DA
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.DA
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.DA
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
# Это одно задание. При выполнении пунктов можно использовать объекты полученные в предыдущих пунктах.
my_dict_1 = {
    "name": "Roma",
    "age": 22,
    "job": "student",
    "family": "mother, father, brother"
}

my_dict_2 = {
    "name": "Oleg",
    "age": 21,
    "food": "pivo",
    "hobby": "nothing"
}

result_same_keys = []
# for same_keys in set(my_dict_1).intersection(set(my_dict_2)):
#     result.append(same_keys)
# print(result)
{result_same_keys.append(same_keys) for same_keys in set(my_dict_1).intersection(set(my_dict_2))}
print(f"Print same keys: {result_same_keys}")

result_only_first_keys = []
{result_only_first_keys.append(only_first_keys) for only_first_keys in set(my_dict_1).difference(set(my_dict_2))}
print(f"Print only first dict keys without second dict keys: {result_only_first_keys}")

dict_only_in_first = {}
for item in result_only_first_keys:
    dict_only_in_first[item] = my_dict_1[item]
print(f"Print pares for first dict without second dict: {dict_only_in_first}")

new_dict = {}

for item in my_dict_1.items():
    if item[0] not in my_dict_2:
        new_dict[item[0]] = item[1]
    else:
        new_dict[item[0]] = [item[1], my_dict_2[item[0]]]

print(f"Print new dictionary: {new_dict}")

# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.


# 1 variant

my_list = ["one", "two", "three", "four", "five"]
new_list = []


def option_list(my_list):
    for numb in range(0, len(my_list)):
        if numb % 2 != 0:
            new_list.append(my_list[numb])
        else:
            new_list.append(my_list[numb][::-1])
    return (new_list)


print(f"Print new list: {option_list(my_list)}")

# 2 variant

my_list = ["one", "two", "three", "four", "five"]


def option_list(my_list):
    new_list = []
    for numb in range(0, len(my_list)):
        new_list.append(my_list[numb][::1 - 2 * (numb % 2)])
    return new_list


print(option_list(my_list))

# 4.Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.случайное_число_от_100_до_999@строка_случайных_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

import random
import string

names = ["Adamson", "Backer", "Carter"]
domains = ["net", "com", "ua"]

length = random.randint(5, 8)


def create_random_numb(length=1):
    for _ in range(1):
        numb = random.randint(100, 1000)
    return numb


def create_random_str(length):
    letters = string.ascii_letters
    rand_string = "".join([random.choice(letters) for _ in range(length)])
    return rand_string


def create_email():
    email = random.choice(names) + "." + str(create_random_numb(length=1)) + "@" + create_random_str(
        length) + "." + random.choice(domains)
    return email


print(f"Your email: {create_email()}")

