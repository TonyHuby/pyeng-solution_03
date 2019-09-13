#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
def parse_sh_ip_int_br(filename):
    result = []
    with open(filename) as open_file:
        for line in open_file:
            res = re.search(r'(\S+).+? (\S+).*(up|down).*(up|down).*', line)
            if res:
                result.append(res.groups())
    return result
print(parse_sh_ip_int_br('sh_ip_int_br.txt'))
