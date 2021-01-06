"""
7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""

n = int(input('Введите натуральное число: '))
sum = 0
for i in range(1, n+1):
    sum += i
sum_n = int(n * (n + 1) / 2)
if sum == sum_n:
    print(f'1+2+...+n = {sum} и n(n+1)/2 = {sum_n}. Для {n} - выражение верно!')
else:
    print(f'1+2+...+n = {sum}, а n(n+1)/2 = {sum_n}. Для {n} - выражение не верно!')
