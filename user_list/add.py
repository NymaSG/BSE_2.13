#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add_users(users):
    name = input("Введите Фамилию и Имя: ")
    phone_number = input("Введите номер телефона: ")
    year = list(map(int, input("Введите дату рождения (Пример: 20 07 2004): ").split()))

    user = {
        'name' : name,
        'phone_number' : phone_number,
        'year' : year
    }

    user.append(user)

    if len(users) > 1:
        users.sort(key=lambda item: item.get('name', '')) 