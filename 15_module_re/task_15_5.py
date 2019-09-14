#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
'''
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
'''
def generate_description_from_cdp(input_file):
    my_dict = {}
    with open(input_file) as in_file:
        for line in in_file:
            reg_search = re.search('(?P<hostname>^\S+).*(?P<local_intf>\w{3} \S+).* (?P<remote_intf>\w{3} \S+)', line)
            if reg_search:
                my_dict[reg_search.group('local_intf')] = 'description Connected to {} port {}'.format(reg_search.group('hostname'), reg_search.group('remote_intf'))
    return my_dict

print(generate_description_from_cdp('sh_cdp_n_sw1.txt'))
