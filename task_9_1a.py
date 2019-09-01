#!/usr/bin/env python

port_security_template = [
            'switchport port-security maximum 2',
            'switchport port-security violation restrict',
            'switchport port-security'
]

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


def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    result = []
    if psecurity:
        access_template = psecurity + access_template 
    else:
        pass
    for intf, intfkey in intf_vlan_mapping.items():
        result.append('interface {}'.format(intf))
        for template in access_template:
            if 'access vlan' in template:
                result.append(str(template) + ' ' + str(intfkey))
            else:
                result.append(template)
    return result

print('\n'.join(generate_access_config(access_config, access_mode_template, port_security_template)))
