#! /usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import re
import yaml
all_sh_cdp = glob.glob('sh_cdp_n*')


def generate_topology_from_cdp(all_files, output_yaml):
    result_line = ''

    for sh_cdp_n in all_files:
        f = open(sh_cdp_n).read()
        result_line += f

    final_text = result_line.split('\n')
    result = {}
    for evr_line in final_text:
        search_hostname = re.search('(\S+)>', evr_line)
        search_neighbours = re.search('(?P<remote_hostname>\S+)\s+(?P<local_intf>(?:G|E)\w{2} \S+).+\s+(?P<remote_intf>(?:G|E)\w{2} \S+)', evr_line)
        if search_hostname:
            connection = {}
            hostname = search_hostname.group(1)
        if search_neighbours:
            remote_conn = {search_neighbours.group('remote_hostname'): search_neighbours.group('remote_intf')}
            connection[search_neighbours.group('local_intf')] = remote_conn
            result[hostname] = connection
    with open(output_yaml, 'w') as f:
        yaml.dump(result, f)
    return result
#find_overlap = re.finditer('\n\S+> ', result_line)
generate_topology_from_cdp(all_sh_cdp, 'out_yaml_file.yaml')

