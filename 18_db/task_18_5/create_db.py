#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
database = 'dhcp_snooping.db'


def create_db(db_name):
    try:
        open_file = open(db_name, 'r')
        print('База существует')
    except FileNotFoundError:
        print('База данных не существует, сечас создам:')
        conn = sqlite3.connect(db_name)
        with open('dhcp_snooping_schema.sql') as sql:
            read_sql = sql.read()
            conn.executescript(read_sql)

create_db(database)
