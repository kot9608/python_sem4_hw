# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит в строку первый список затем на следующией строке второй список.



lst1 = list(map(int, input("Введите 1й список чисел через пробел: ").split()))
lst2 = list(map(int, input("Введите 2й список чисел через пробел: ").split()))

union_lst = list(set(lst1) & set(lst2))
if len(union_lst)==0:
    print('Пересечений нет')
else:
    union_lst.sort()
    print(union_lst)