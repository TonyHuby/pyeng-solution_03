#!/usr/bin/env python
with open('CAM_table.txt', 'r') as cam_table:
    for line in cam_table:
        if len(line.split('.')) == 3:
            cam = line.split()
            out_p = '{:10} {:20} {:10}'
            print(out_p.format(cam[0],cam[1],cam[3]))
        else:
            pass

