#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import module_1 as md 

if __name__ == "__main__":
    type_param = input("Введите тип (list/tuple): ")
    numbers_string = input("Введите ваши переменные: ")

    converter = md.create_converter(type_param)

    result = converter(numbers_string)

    print(result)
