# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


x = input('Введите число ')

def summa(x):                            
    if float(x) < 0:                            
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f'Сумма чисел равна {summa(x)}')


# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('input N: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print(factorial, end=' ')


# 3. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

n = int(input("Введите число n: "))
s = 0
for i in range(1,n+1):
    s += (1+1/i)**i
print(f"Полученная сумма последовательности (1+1/n)^n равнна {round(s,2)}")  



# '4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Number of elements: ', get_numbers(numbers))

x = int(input('Enter  position of first element: '))
y = int(input('Enter position of second element: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)

# 5. Реализовать алгоритм перемешивания списка

import random

def get_list(n, lft, rght):
    return [random.randint(lft, rght) for i in range(n)]

def shuffle_list(lst):
    return random.shuffle(lst)

n = 10
lft = -20
rght = 50

mylist = get_list(n, lft, rght)
print(mylist)
shuffle_list(mylist)
print(mylist)