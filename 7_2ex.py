#!/usr/bin/env python
ignore = ['duplex', 'alias', 'Current configuration']


with open('./07_files/config_sw1.txt', 'r') as config_sw1:
    for line in config_sw1:
        for ig_l in ignore:
            if line.count(ig_l) == 0:
                pass
            else:
                line = '!'
        if line.startswith('!'):
            pass
        else:
            print(line.rstrip())
