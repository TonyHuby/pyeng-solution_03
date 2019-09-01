#!/usr/bin/env python

def get_int_vlan_map(config_filename):
    trunk_int = {}
    access_int = {}
    with open(config_filename, 'r') as conf_line:
        for line in conf_line:
            if line.startswith('interface'):
                intf = line.split()[1]
            elif 'allowed vlan' in line:
                vlans = line.split()[-1].split(',')
                ivlan = []
                for vlan in vlans:
                    ivlan.append(int(vlan))
                trunk_int.update({intf:ivlan})
            elif 'mode access' in line:
                access_int.update({intf: 1})
            elif 'access vlan' in line:
                access_vln = int(line.split()[-1])
                access_int.update({intf:access_vln})

    return access_int, trunk_int

result = get_int_vlan_map('config_sw2.txt')
print(result)



