#!/usr/bin/env python

 
#cdpn = open('sh_cdp_n_sw1.txt', 'r')
#local_name = cdpn.read().split('>')[0][1:]
#sep_cdp = open('sh_cdp_n_sw1.txt', 'r').read().split('\n')[7:]
#result =  {}
def parse_cdp_neighbors(command_output):
    cdpn = open(command_output, 'r')
    local_name = cdpn.read().split('>')[0].strip('\n')
    open_cdp = open(command_output, 'r').read().split('\n')
    line_num = 0
    for cdp_line in open_cdp:
        if 'Device ID' in cdp_line:
            line_num += 1
            break
        else:
            line_num += 1
    sep_cdp = open_cdp[line_num:]
    result =  {}
    for line in sep_cdp:
        if len(line) > 1:
            local_int = '{}{}'.format(line.split()[1:2][0], line.split()[2:3][0])
            remote_int = '{}{}'.format(line.split()[-2:-1][0], line.split()[-1])
            remote_name = line.split()[0]
            local_unit = (local_name, local_int)
            remote_unit = (remote_name, remote_int)
            result[local_unit] = remote_unit
    return result
result = (parse_cdp_neighbors('sh_cdp_n_r2.txt'))
[print(res) for res in result.items()]


#def parse_cdp_neighbor(command_output):

