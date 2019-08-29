#!/usr/bin/env python


london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

name = input('Enter Device name: ')
namelist = str(london_co[name].keys())
nameout = namelist.replace('dict_keys','').strip('(,)').replace('\'','').replace('\'','').strip('[]')
print('Enter parameter (',nameout,'): ') 
param = input()

print(london_co[name][param])
