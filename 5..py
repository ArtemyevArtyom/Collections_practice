"""
Задание №5
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""
lst = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5]
res = []
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        res.append(i + 1)
print(res)

res2 = [i + 1 for i in range(len(lst)) if lst[i] % 2 == 1]
print(res2)
