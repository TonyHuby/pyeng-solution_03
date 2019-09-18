#! /usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import graphviz
from draw_network_graph import draw_topology
'''
Задание 17.2b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_2b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

with open('topology.yaml', 'r') as f: 
        topology = yaml.safe_load(f) 
def transform_topology(i_topology):
    result = {} 
    for m_key in i_topology.keys(): 
        for intf_key in i_topology[m_key].keys(): 
            for re_host, re_port in i_topology[m_key][intf_key].items(): 
                if (re_host, re_port) not in result.keys():
                    result[(m_key, intf_key)] = (re_host, re_port)
    return result
#print(transform_topology(topology))
draw_topology(transform_topology(topology))
