#!/usr/bin/env python
# -*- coding: utf-8 -*-

ip_addr = input('Input IP address in format x.x.x.x: ')
spl_ip = ip_addr.split('.')
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
