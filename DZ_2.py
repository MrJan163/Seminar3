# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом


str_num = input()
if str_num.isdecimal() or str_num.isalpha():
    print('no')
else:
    print('yes')