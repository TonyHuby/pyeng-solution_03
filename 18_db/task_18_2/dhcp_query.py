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
    result = conn.execute('select * from dhcp')
    out_line = 'В таблице dhcp такие записи:'
    print(out_line)
    return tabulate(result)

def select_query(name, parameter):
    conn = sqlite3.connect(database)
    if name == 'vlan':
        outline = 'Информация об устройстве с такими параметрами: vlan '+ str(parameter)
        quer = "select * from dhcp where vlan = "+str(parameter)
        result = conn.execute(quer)
    else:
        outline = 'Информация об устройстве с такими параметрами: '+ name + ' ' + parameter
        result = conn.execute('select * from dhcp where '+name+' ='+"'"+parameter+"'")
        print(outline)
    return tabulate(result)

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
    except:
        print('LOL')


