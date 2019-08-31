#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = 0
result = 1

ip_addr = input('Input IP address in format x.x.x.x: ')
spl_ip = ip_addr.split('.')

if len(spl_ip) != 4:
    result = 0
else:
    for octet in spl_ip:
        if octet.isdigit():
            if int(octet) in range(0,256):
                pass
            else:
                result = 0
        else:
            result = 0

if result != 0:
    if int(spl_ip[0]) in range(1,224):
        print('unicast')
    elif int(spl_ip[0]) in range(224,240):
        print('multicast')
    elif int(spl_ip[0]) == 255 and int(spl_ip[1]) == 255 and int(spl_ip[2]) == 255 and int(spl_ip[3]) == 255:
        print('local broadcast')
    elif int(spl_ip[0]) == 0 and int(spl_ip[1]) == 0 and int(spl_ip[2]) == 0 and int(spl_ip[3]) == 0:
        print('unassigned')
    else:
        print('unused')
else:
    print('Wrong IP address')
