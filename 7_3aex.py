#!/usr/bin/env python
all_list = []
all_list.sort()
with open('CAM_table.txt', 'r') as cam_table:
    for line in cam_table:
        if len(line.split('.')) == 3:
            all_list.append(line)
        else:
            pass
 
all_list.sort()
out_p = '{:10} {:20} {:10}'
for lines in all_list:
    cam = lines.split()
    if cam[0] == '1000':
        last_s = cam
    else:
        print(out_p.format(cam[0],cam[1],cam[3]))
print(out_p.format(last_s[0],last_s[1],last_s[3]))
