# 3.10 Вводим с клавиатуры десятичное число.
# Необходимо перевести его в шестнадцатиричную систему счисления.


num = int(input("Введите число: "))
values = '0123456789ABCDEF'
num_in_16 = ''
while(num > 0):
    num_in_16 = values[num % 16] + num_in_16
    num//= 16
print(num_in_16)