#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import netmiko

command = 'sh ip int br'

def send_show_command(command):
    with open('devices.yaml', 'r') as devices_yaml:
        devices = yaml.safe_load(devices_yaml)
        result = ''
        for device in devices:
            try:
                with netmiko.ConnectHandler(**device) as ssh:
                    print('Connect to {}'.format(device['ip']))
                    res = '\nCommand output on {}\n'.format(device['ip']) + ssh.send_command(command)
                    result += res
            except netmiko.NetMikoAuthenticationException as err: 
                print(err)
        return result

print(send_show_command(command))
