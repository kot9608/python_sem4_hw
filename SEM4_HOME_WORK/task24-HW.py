# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 1 3 2 1 1 6
# Output: 10

# СРЕЗЫ!!!

#1 2 3 4 5

lst = list(map(int, input("Введите количество ягод на каждом кусте через пробел: ").split()))
sum = 0
sum_max = 0
i=0#счётчик
while i < len(lst):
    lst_i=lst[i:] + lst[:i]#смещаем введённый массив к началу. Не придумал, как это сделать через i и счётчик
    # a=lst_i[i]
    # b=int(lst_i[(i+1)])
    # c=lst_i[i+2]
    sum=lst_i[0]+lst_i[1]+lst_i[2]
    i+=1
    if sum>sum_max:
        sum_max=sum
print(sum_max)



#print(lst[0+(len(lst))-1])