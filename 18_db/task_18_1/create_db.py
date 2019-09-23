#! /usr/bin/env python
import sqlite3

def check_db(db_name):
    try:
        open_file = open(db_name, 'r')
    except FileNotFoundError:
        print('''Такой Базы данных не существует
Сейчас создам...''')
        conn = sqlite3.connect(db_name)
        with open('dhcp_snooping_schema.sql', 'r') as the_file:
            schema = the_file.read()
            conn.executescript(schema)
    else:
        print('База данных существует')
        open_file.close()

check_db('dhcp_snooping.db')
