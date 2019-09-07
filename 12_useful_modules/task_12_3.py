#!/usr/bin/env python
from task_12_1 import ping_ip
from tabulate import tabulate
from sys import argv

resultat = ['1.1.1.1','2.2.2.2','8.8.4.4','12.12.32.12']
def print_ip_table(a_ip):
    colums = ['Reachable', 'Unreachable']
    if len(a_ip[0]) > len(a_ip[1]):
        for smth in range(len(a_ip[0]) - len(a_ip[1])):
            a_ip[1].append('')
    elif len(a_ip[0]) < len(a_ip[1]):
        for smth in range(len(a_ip[1]) - len(a_ip[0])):
            a_ip[0].append('')
    else: pass
    result = list(zip(a_ip[0],a_ip[1]))
    print(tabulate(result, headers = colums))


s = ping_ip(*argv[1:])
print_ip_table(s)
