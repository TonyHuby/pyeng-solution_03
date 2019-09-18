#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
file_read = open('sh_cdp_n_sw1.txt').read()


def parse_sh_cdp_neighbors(n_output):
    result = {}
    res_list = re.finditer('\n(\w+) \s+(\S+ \S+) .+(\w{3} \S+)', n_output)
    res_hostname = re.search('\n(\w+)>', n_output).group(1)
    for line in res_list:
        remote_dev = {line.group(1): line.group(3)}
        local_dev = {line.group(2): remote_dev}
        result.update(local_dev)
    return_me = {}
    return_me[res_hostname] = result
    return return_me

print(parse_sh_cdp_neighbors(file_read))
