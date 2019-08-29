#!/usr/bin/env python

imode = input('Enter interface mode (access/trunk): ')
itype = input('Enter interface type (Fa0/0): ')

itext = {}
itext['access'] = ['Enter vlan number: ']
itext['trunk'] = ['Enter vlans range: ']
outitext = str(itext[imode]) 

ivlan = input(str(outitext).strip('[]').strip('\'\''))

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

interfaces = {}
interfaces['access'] = access_template
interfaces['trunk'] = trunk_template

print('interface {}'.format(itype))
x='\n'.join(interfaces[imode])
print(str(x).format(ivlan))
