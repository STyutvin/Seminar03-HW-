# Задача №1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Список чисел зададим случайным образом, введя количество его элементов.
from random import randint
some_list = []
i = 1
n = int(input('Введите количество элементов в списке: '))
for i in range(n):
    some_list.append(randint(1,5))
    i += 1
print(f'Ваш случайно сгенерированный список из {n} элементов: {some_list}')
j=1
sum=0
while j< len(some_list):
    sum=sum+some_list[j]
    j+=2
print(f'Сумма элементов списка, стоящих на нечётной позиции: {sum}')