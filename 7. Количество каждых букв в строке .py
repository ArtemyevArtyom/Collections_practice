"""
Задание №7
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
"""

data = 'is do is'
my_dict = {}
for el in data:
    if el.isalpha(): #.isalpha Вернёт True, если в строке хотя бы один символ и все символы строки являются буквами, иначе — False.
        my_dict[el] = data.count(el)
print(my_dict)

my_dict = {el: data.count(el) for el in data if el.isalpha()}
print(my_dict)

my_dict = {}
for el_1 in data:
    if el_1.isalpha():
        count = 0
        for el_2 in data:
            if el_1 == el_2:
                count += 1
        my_dict[el_1] = count

print(my_dict)

my_dict = {}
for el in data:
    if el.isalpha():
        my_dict[el] = my_dict.get(el, 0) + 1
print(my_dict)