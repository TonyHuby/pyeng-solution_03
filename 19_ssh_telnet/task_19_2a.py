#!/usr/bin/env python
# -*- coding: utf-8 -*-
import netmiko
import yaml

device = {'device_type': 'cisco_ios',
          'ip': '192.168.100.1',
          'username': 'cisco',
          'password': 'cisco'}

commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]

def send_config_commands(yaml_device, config_commands, verbose=True):
    with open('devices.yaml', 'r') as yaml_file:
        devices = yaml.safe_load(yaml_file)
        result = ''
        for device in devices:
            if verbose:
                print('Connecting to {}...'.format(device['ip']))
            with netmiko.ConnectHandler(**device) as ssh:
                res = ssh.send_config_set(config_commands)
                result += '\n Device {} configurated: \n'.format(device['ip']) + res
    return result

print(send_config_commands(device, commands, verbose=False))
