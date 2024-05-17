#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def create_converter(type_param):
    def converter(input_string):
        numbers = list(map(int, input_string.split()))
        if type_param == 'list':
            return numbers
        else:
            return tuple(numbers)
    return converter