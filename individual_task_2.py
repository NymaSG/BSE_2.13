#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Выполнить индивидуальное задание лабораторной работы 2.8, оформив все классы программы в виде отдельного пакета.
#Разработанный пакет должен быть подключен в основную программу с помощью одногоиз вариантов команды import .
#Настроить соответствующим образомпеременную __all__ в файле __init__.py пакета.


from user_list import add, select, checklist


if __name__ == "__main__":
    users = []

    while True:
        command = input("$ ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            add.add_users(users)

        elif command == 'select':
            checklist.checklist_users(users)

        elif command == 'list':
            select.select_user(users)