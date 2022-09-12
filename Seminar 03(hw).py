# Задача №1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Список чисел зададим случайным образом, введя количество его элементов.
# from random import randint
# some_list = []
# i = 1
# n = int(input('Введите количество элементов в списке: '))
# for i in range(n):
#     some_list.append(randint(1,5))
#     i += 1
# print(f'Ваш случайно сгенерированный список из {n} элементов: {some_list}')
# j=1
# sum=0
# while j< len(some_list):
#     sum=sum+some_list[j]
#     j+=2
# print(f'Сумма элементов списка, стоящих на нечётной позиции: {sum}')
#-----------------------------------------------------------

# Задача №2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint
# some_list = []
# i = 1
# n = int(input('Введите количество элементов в списке: '))
# for i in range(n):
#     some_list.append(randint(1,5))
#     i += 1
# print(f'Ваш случайно сгенерированный список из {n} элементов: {some_list}')
# k=0
# j=1
# if n%2==0:
#     while k<len(some_list)//2:
#         mult=some_list[k]*some_list[len(some_list)-j]
#         print(mult)
#         k+=1
#         j+=1
# else:
#     while k<len(some_list)//2:
#         mult=some_list[k]*some_list[len(some_list)-j]
#         print('Произведения пар чисел списка:')
#         print(mult)
#         print(some_list[len(some_list)//2]**2)
#         k+=1
#         j+=1
#-----------------------------------------------------------

#Задайте список из вещественных чисел. Напишите программу, которая найдёт  между максимальным и минимальным значением дробной части элементов.
some_list=[1.1, 1.2, 3.3, 5, 10.4]
print(f'Текущий список {some_list}')
#new_list=[]
new_list=list(map(float, some_list))
second_list=[round(i%1,2) for i in new_list if i%1 != 0]
print(f'Разница между max и min значениями дробной части {round(max(second_list)-min(second_list),2)}')
#-----------------------------------------------------------