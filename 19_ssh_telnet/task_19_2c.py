#!/usr/bin/env python
# -*- coding: utf-8 -*-

import netmiko
import yaml
import re

# списки команд с ошибками и без:
commands_with_errors = ['logging 0255.255.1', 'logging', 'sh i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands

device = {'device_type': 'cisco_ios',
          'ip': '192.168.100.1',
          'username': 'cisco',
          'password': 'cisco'}

def send_config_commands(yaml_device, config_commands, verbose=True):
    with open('devices.yaml', 'r') as yaml_file:
        devices = yaml.safe_load(yaml_file)
        result = []
        good = {}
        bad = {}
        for device in devices:
            if verbose:
                print('Connecting to {}...'.format(device['ip']))
            with netmiko.ConnectHandler(**device) as ssh:
                for command in config_commands:
                    res = ssh.send_config_set(command)
                    if 'Ambiguous command' in res:
                        bad[command] = res
                        err = re.search('.*(Ambiguous command:.*?\n).*', res) 
                        print('Command {} execute with error {} on device {}'.format(command, err.group(1), device['ip']))
                        cont = input('Continue execute process? [y]/n: ')
                        if cont == 'n' or cont == 'no':
                            break
                    elif 'Incomplete command' in res:
                        bad[command] = res
                        err = re.search('.*(Incomplete command\.).*', res)
                        print('Command {} execute with error {} on device {}'.format(command, err.group(1), device['ip']))
                        cont = input('Continue execute process? [y]/n: ')
                        if cont == 'n' or cont == 'no':
                            break
                    elif 'Invalid input detected' in res:
                        bad[command] = res
                        err = re.search('.*(Invalid input detected.*marker\.).*', res)
                        print('Command {} execute with error {} on device {}'.format(command, err.group(1), device['ip']))
                        cont = input('Continue execute process? [y]/n: ')
                        if cont == 'n' or cont == 'no':
                            break
                    else:
                        good[command] = res
                res_dev = (good, bad)
                result.append(res_dev)
    return result

parser = send_config_commands(device, commands, verbose=True)
for m in parser:
    a,b = m
    print('\n')
    print(a.keys())
    print(b.keys())

