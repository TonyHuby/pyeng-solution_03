#!/usr/bin/env python
# -*- coding: utf-8 -*-
from draw_network_graph import draw_topology
def create_network_map(*cdp_files):
    result =  {}
    for cdp_file in cdp_files:
        cdpn = open(cdp_file, 'r')
        local_name = cdpn.read().split('>')[0].strip('\n')
        line_num = 0
        open_cdp = open(cdp_file, 'r').read().split('\n')
        for cdp_line in open_cdp:
            if 'Device ID' in cdp_line:
                line_num += 1
                break
            else:
                line_num +=1
        sep_cdp = open_cdp[line_num:]
        for line in sep_cdp:
            if len(line) > 1:
                local_int = '{}{}'.format(line.split()[1:2][0], line.split()[2:3][0])
                remote_int = '{}{}'.format(line.split()[-2:-1][0], line.split()[-1])
                remote_name = line.split()[0]
                local_unit = (local_name, local_int)
                remote_unit = (remote_name, remote_int)
                if remote_unit not in result.keys():
                    result[local_unit] = remote_unit
    return result
result = (create_network_map('sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt'))
#[print(res) for res in result.items()]
draw_topology(result)


