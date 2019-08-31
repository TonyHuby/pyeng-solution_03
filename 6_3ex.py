#!/usr/bin/env python

access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}
trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17', '25']
    }

for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

for interface, vlans in trunk.items():
    print('interface FasEthernet' + interface)
    for tcommand in trunk_template:
        if tcommand.endswith('allowed vlan'):
            if vlans[0] == 'add':
                addstring = ' {} add '.format(tcommand)
                for vl in vlans[1:]:
                    addstring = addstring + str(vl) + ','
                print(addstring[:-1])
            elif vlans[0] == 'del':
                delstring = ' {} remove '.format(tcommand)
                for vl in vlans[1:]:
                    delstring = delstring + str(vl) + ','
                print(delstring[:-1])
            elif vlans[0] == 'only':
                onlystring = ' {} '.format(tcommand)
                for vl in vlans[1:]:
                    onlystring = onlystring + str(vl) + ','
                print(onlystring[:-1])
        else:
            print(' {}'.format(tcommand))
