#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sqlite3
import yaml
import glob

all_sw = glob.glob('sw*.txt')
def open_test(db_name):
    try:
        open_db = open(db_name, 'r')
    except FileNotFoundError:
        return False
    else:
        open_db.close()
        return True

def insert_switches(db_name):
    if open_test(db_name):
        print('Добавляю информацию по коммутаторам в БД, я быстро...')
        conn = sqlite3.connect(db_name)
        query = 'insert into switches values(?, ?)'
        with open('switches.yml') as yaml_file:
            import_yaml = yaml.safe_load(yaml_file)
        for hostname, location in import_yaml['switches'].items():
            stup = (hostname, location)
            try:
                conn.execute(query, stup)
            except sqlite3.IntegrityError as err:
                print('Не могу добавить данные: ', stup, ' Возникла ошибка: ', err)
        conn.commit()
        conn.close()
    else:
        print('Такой Базы данных не существует, перед добавлением файлов требуется создать DB')


def insert_snoop_data(*args, db_name):
    if open_test(db_name):
        groups = {}
        conn = sqlite3.connect(db_name)
        set_zero = 'update dhcp set active = 0'
        conn.execute(set_zero)
        query = 'insert or replace into dhcp(mac, ip, vlan, interface, switch, active) values (?, ?, ?, ?, ?, 1)'
        print('Добавляю информацию из dhcp snooping table...')
        for sw_files in args:
            for sw_file in sw_files:
                result = []
                hostname = sw_file[:3]
                with open(sw_file) as re_file:
                    open_re_file = re_file.read()
                    read_iter = re.finditer('\n(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})\s+(\d+\.\d+\.\d+\.\d+)\s+\S+\s+\S+\s+(\d+)\s+(\S+)', open_re_file)
                    for ever_iter in read_iter:
                        result.append(ever_iter.groups())
                        groups[hostname] = result
        for key in groups.keys():
            for res in groups[key]:
                re_list = list(res)
                re_list.append(key)
                try: 
                    conn.execute(query, re_list)
                except sqlite3.IntegrityError as err:
                    print('Не могу добавить данные: ', re_list, ' Возникла ошибка: ', err)
        conn.commit()
        conn.close()

insert_switches('dhcp_snooping.db')
insert_snoop_data(all_sw, db_name='dhcp_snooping.db')
