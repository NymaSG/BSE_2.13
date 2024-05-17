#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def select_user(users):
    print('Введите числов месяца (1-12): ')
    while True:
        num = int(input())
        if num < 1 or num > 12:
            print('Значение введено неправильно! Попробуйте еще раз.')
        else:
            break
    
    line = '+-{}-+-{}-+-{}-+-{}-+'.format('-' * 4, '-' * 20, '-' * 18, '-' * 10)
    print(line)
    print('| {:ˆ4} | {:ˆ20} | {:ˆ18} | {:ˆ10} |'.format(
        '№' , 
        'Название' , 
        'Номер телефона',
        'Дата'
    ))
    print(line)

    for idx, user in enumerate(users, 1):
        if user['year'][1] == num:
            print('| {:ˆ4} | {:ˆ20} | {:ˆ18} | {:ˆ10} |'.format(
                idx,
                user['name'],
                user['phone_number'],
                ''.join(map(str, user['year']))
                )
            )
            print(line)