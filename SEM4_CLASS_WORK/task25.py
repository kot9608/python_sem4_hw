# Задача №25. Общее обсуждение
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


lst = list(input("Введите массив букв через пробел: ").split())
print(lst)
alfavit = {}
for i in lst:
    if i in alfavit.keys():
        alfavit[i] = alfavit[i]+1
    else:
        alfavit[i] = 0
    if alfavit[i] == 0:
        print(f'{i}', end=' ')
    else:
        print(f'{i}_{alfavit[i]}', end=' ')
