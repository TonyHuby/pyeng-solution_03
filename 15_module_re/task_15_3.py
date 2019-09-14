#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
'''
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
'''
def convert_ios_nat_to_asa(source_file, destination_file): 
    out_str = ['object network LOCAL_{}',
            ' host {}',
            ' nat (inside,outside) static interface service {} {} {}\n']
    out_str_f = '\n'.join(out_str)
    df = open(destination_file, 'w')
    with open(source_file, 'r') as sf:
        for line in sf:
            reg_for_source = re.search('.+(?P<protocol>udp|tcp|ip).*?(?P<s_ip>\d+\.\d+\.\d+\.\d+).*?(?P<s_port>\d+).*?\S+.*?\S+.+?(?P<d_port>\d+).*', line)
            print(reg_for_source.group('s_ip'))
            df.write(out_str_f.format(reg_for_source.group('s_ip'),reg_for_source.group('s_ip'),reg_for_source.group('protocol'),reg_for_source.group('s_port'),reg_for_source.group('d_port')))
    df.close()
    


convert_ios_nat_to_asa('cisco_nat_config.txt', 'test_cfg.txt')

