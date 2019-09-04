#!/usr/bin/env python
# -*- coding: utf-8 -*-
from draw_network_graph import draw_topology
'''
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
def create_network_map(*cdp_files):
    result =  {}
    for cdp_file in cdp_files:
        cdpn = open(cdp_file, 'r')
        local_name = cdpn.read().split('>')[0].strip('\n')
        line_num = 0
        open_cdp = open(cdp_file, 'r').read().split('\n')
        for cdp_line in open_cdp:
            if 'Device ID' in cdp_line:
                line_num += 1
                break
            else:
                line_num +=1
        sep_cdp = open_cdp[line_num:]
        for line in sep_cdp:
            if len(line) > 1:
                local_int = '{}{}'.format(line.split()[1:2][0], line.split()[2:3][0])
                remote_int = '{}{}'.format(line.split()[-2:-1][0], line.split()[-1])
                remote_name = line.split()[0]
                local_unit = (local_name, local_int)
                remote_unit = (remote_name, remote_int)
                if remote_unit not in result.keys():
                    result[local_unit] = remote_unit
    return result
result = (create_network_map('sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt'))
#[print(res) for res in result.items()]
draw_topology(result)


