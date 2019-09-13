#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def get_ip_from_cfg(filename):
    itogo = {}
    with open(filename) as lfile:
        for line in lfile:
            res_int = re.search(r'^interface (\S+).*', line)
            res_ip = re.search(r' ip address (\S+) (\S+).+', line)
            if res_int:
                a = res_int.group(1)
            if res_ip: 
                itogo[a] = res_ip.groups() 
    return itogo

print(get_ip_from_cfg('config_r1.txt'))


