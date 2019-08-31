#!/usr/bin/env python

with open('ospf.txt') as ospf:
    for ospf_line in ospf:
        ols = ospf_line.split()
        olsstring = '{:20} {:20}\n{:20} {:20}\n{:20} {:20}\n{:20} {:20}\n{:20} {:20}\n{:20} {:20}'
        print(olsstring.format('Protocol: ', ols[0]+'SPF', 'Prefix: ', ols[1], 'AD/Metric:', ols[2].strip('[]'), 'Next-Hop:', ols[4].strip(','), 'Last Update:', ols[5].strip(','), 'Outbound Interface:', ols[6]))
        print('-'*40)

