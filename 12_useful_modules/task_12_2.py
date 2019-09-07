#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ipaddress

def convert_ranges_to_ip_list(*args):
    long_hosts = []
    for ip_a in args:
        ip_split = ip_a.split('-')
        if len(ip_split) > 1 :
            if len(ip_split[1].split('.')) > 1:
                last_octet = int(ip_split[1].split('.')[-1]) + 1
                octet_list = range(int(ip_split[0].split('.')[-1]), last_octet)
                for octet in list(octet_list):
                    res = ''
                    splitted = ip_split[1].split('.')
                    splitted[-1] = octet
                    for oc in splitted:
                        res = str(res) + str(oc) + '.'
                    long_hosts.append(res.strip('.'))
            else:
                last_octet = int(ip_split[-1]) + 1
                octet_list = range(int(ip_split[0].split('.')[-1]), last_octet)
                for octet in list(octet_list):
                    res = ''
                    splitted = ip_split[0].split('.')
                    splitted[-1] = octet
                    for oc in splitted:
                        res = str(res) + str(oc) + '.'
                    long_hosts.append(res.strip('.'))
        else:
            long_hosts.append(ip_a)
    return long_hosts

print(convert_ranges_to_ip_list('10.1.1.1-10', '172.16.20.20', '192.168.43.1-192.168.43.12'))


