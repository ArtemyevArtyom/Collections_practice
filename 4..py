"""
Задание №4
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""
u_list = [3, 4, 5, 4, 3, 2]
print(*u_list)

new_lst = [el for el in u_list if u_list.count(el) != 2]

print(*new_lst)
