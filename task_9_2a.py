# -*- coding: utf-8 -*-

trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}
def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result = {}
    for intf, keys in intf_vlan_mapping.items():
        strkey = ''
        intfname = 'interface ' + intf
        result.update({intf: [intfname]})
        for key in keys:
            strkey = str(strkey) + str(key) + ','
        for trunk in trunk_template:
            if 'allowed vlan' in trunk:
                    result[intf].append(trunk + ' ' + strkey)
            else: 
                result[intf].append(trunk)
    return result

generate = generate_trunk_config(trunk_config, trunk_mode_template)
#print( generate)
