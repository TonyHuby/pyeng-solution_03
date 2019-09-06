#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess

def ping_ip(*args):
    success = []
    false = []
    for ip_host in args:
        print('ping for host ', ip_host)
        result = subprocess.run('ping {} -c 1'.format(ip_host), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        if result.returncode == 0:
            success.append(ip_host)
        else:
            false.append(ip_host)
        res = (success, false)
    return res

print(ping_ip('1.1.1.1','2.2.2.2','8.8.4.4','12.12.32.12'))

