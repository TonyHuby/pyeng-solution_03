#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Description of the script
'''
import sqlite3
import argparse
from tabulate import tabulate
database = 'dhcp_snooping.db'


def full_query():
    conn = sqlite3.connect(database)
    result_active = conn.execute('select * from dhcp where active = 1').fetchall()
    result_inactive = conn.execute('select * from dhcp where active = 0').fetchall()
    out_line = 'В таблице dhcp такие записи:'
    print(out_line)
    if len(result_active) > 0 and len(result_inactive) > 0:
        print('Активные записи:')
        print (tabulate(result_active))
        print('Неактивные записи:')
        return tabulate(result_inactive)
    elif len(result_active) > 0:
        result_active = conn.execute('select * from dhcp where active = 1')
        print('Активные записи:')
        return tabulate(result_active)
    elif len(result_inactive) > 0:
        result_inactive = conn.execute('select * from dhcp where active = 0')
        print('Неактивные записи:')
        return tabulate(result_inactive)


def select_query(name, parameter):
    conn = sqlite3.connect(database)
    if name == 'vlan':
        outline = 'Информация об устройстве с такими параметрами: vlan '+ str(parameter)
        quer_active = "select * from dhcp where vlan = {} and active = 1".format(str(parameter))
        quer_inactive = "select * from dhcp where vlan = {} and active = 0".format(str(parameter))
        result_active = conn.execute(quer_active).fetchall()
        result_inactive = conn.execute(quer_inactive).fetchall()
    else:
        outline = 'Информация об устройстве с такими параметрами: '+ name + ' ' + parameter
        result_active = conn.execute('select * from dhcp where \'{}\' = \'{}\' and active = 1'.format(name, parameter)).fetchall()
        result_inactive = conn.execute('select * from dhcp where \'{}\' = \'{}\' and active = 0'.format(name, parameter)).fetchall()
    print(outline)
    if len(result_active) > 0 and len(result_inactive) > 0:
        print('Активные записи:')
        print (tabulate(result_active))
        print('Неактивные записи:')
        return tabulate(result_inactive)
    elif len(result_active) > 0:
        print('Активные записи')
        return tabulate(result_active)
    elif len(result_inactive) > 0:
        print('Нективные записи')
        return tabulate(result_inactive)

def select_vlan(args):
    name = 'vlan'
    print(select_query(name, args.vlan))

def select_mac(args):
    name = 'mac'
    print(select_query(name, args.mac))

def select_interface(args):
    name = 'interface'
    print(select_query(name, args.interface))

def select_ip(args):
    name = 'ip'
    print(select_query(name, args.ip))

def select_switch(args):
    name = 'switch'
    print(select_query(name, args.switch))

parser = argparse.ArgumentParser(description = 'Параметры для запроса в БД')
subparsers = parser.add_subparsers(title = 'subcommands',
                                    description = 'valid commands',
                                    help = 'find data in database')
ip_parser = subparsers.add_parser('ip', help='use decimial format like 10.10.10.1')
ip_parser.add_argument('ip', help = 'ip address')
ip_parser.set_defaults(func=select_ip)
vlan_parser = subparsers.add_parser('vlan', help='use integer')
vlan_parser.add_argument('vlan', help='vlan number')
vlan_parser.set_defaults(func=select_vlan)
interface_parser = subparsers.add_parser('interface', help='use full name')
interface_parser.add_argument('interface', help='interface number')
interface_parser.set_defaults(func=select_interface)
mac_parser = subparsers.add_parser('mac', help='use : for decilimiter')
mac_parser.add_argument('mac', help='mac address')
mac_parser.set_defaults(func=select_mac)
switch_parser = subparsers.add_parser('switch', help='switch hostname')
switch_parser.add_argument('switch', help='hostname')
switch_parser.set_defaults(func=select_switch)

#args = parser.parse_args()
#vars(args)
if __name__ == '__main__':
    try:
        args = parser.parse_args()
        if not vars(args):
            print(full_query())
        elif len(vars(args)) == 2:
            args.func(args)
    except ValueError:
        print('LOL')
