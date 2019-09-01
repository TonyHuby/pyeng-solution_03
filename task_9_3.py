#!/usr/bin/env python

def get_int_vlan_map(config_filename):
    trunk_int = {}
    access_int = {}
    with open(config_filename, 'r') as conf_line:
        for line in conf_line:
            if line.startswith('interface'):
                spl_line = line.split()
                intf = spl_line[1]
            elif 'allowed vlan' in line:
                spl_line = line.split()
                vlans = spl_line[-1].split(',')
                ivlan = []
                for vlan in vlans:
                    ivlan.append(int(vlan))
                trunk_int.update({intf:ivlan})
            elif 'access vlan' in line:
                spl_line = int(line.split()[-1])
                access_int.update({intf:spl_line})

    return access_int, trunk_int

result = get_int_vlan_map('config_sw1.txt')
print(result)



