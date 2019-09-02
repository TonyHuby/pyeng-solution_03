#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def convert_config_to_dict(config_filename):
    with open(config_filename) as conf_file:
        final_dict = {}
        for line in conf_file:
            if line.startswith('!'):
                pass
            elif ignore_command(line, ignore):
                pass
            elif not line.startswith(' '):
                dict_list = []
                lname = line
                final_dict.update({lname:dict_list})
            else:
                dict_list.append(line)
                final_dict.update({lname:dict_list})

    return final_dict

res = convert_config_to_dict('config_sw1.txt')

for name, uses in res.items():
    print (name, uses)

#print(res.items())
