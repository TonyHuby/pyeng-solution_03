#!/usr/bin/env python

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}


def generate_access_config(intf_vlan_mapping, access_template):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    result = []
    for intf, intfkey in intf_vlan_mapping.items():
        result.append('interface {}'.format(intf))
        result.append(access_template[0])
        result.append(str(access_template[1]) + ' ' + str(intfkey))
        result.append(access_template[2])
        result.append(access_template[3])
        result.append(access_template[4])
    return result

print(generate_access_config(access_config, access_mode_template))
