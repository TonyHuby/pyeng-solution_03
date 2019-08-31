#!/usr/bin/env python
all_list = []
vlan_num = input('Input vlan number: ')
with open('CAM_table.txt', 'r') as cam_table:
    for line in cam_table:
        if len(line.split('.')) == 3:
            all_list.append(line)
        else:
            pass
 
out_p = '{:10} {:20} {:10}'
for lines in all_list:
    cam = lines.split()
    if cam[0] == vlan_num:
        print(out_p.format(cam[0],cam[1],cam[3]))
    else:
        pass
