#!/usr/bin/env python
import sys

network = sys.argv[1]

addr = network.split('.')
mask = addr[3].split('/')
addr[3] = mask[0]

#MASK MAGIC
zeros = 32 - int(mask[1])
binmask = int(mask[1])*'1' + zeros*'0'

#NETWORK MAGIC
binaddr = '{:08b}'.format(int(addr[0]))+'{:08b}'.format(int(addr[1]))+'{:08b}'.format(int(addr[2]))+'{:08b}'.format(int(addr[3]))
binout = binaddr[:-zeros] + zeros * '0'

output_n = ['\nNetwork:',
'{:<8} {:<8} {:<8} {:<8}',
'{:08b} {:08b} {:08b} {:08b}']

output_m = ['\nMask:', '/{:8}', '{:<8} {:<8} {:<8} {:<8}', '{:<8} {:<8} {:<8} {:<8}']

print('\n'.join(output_n).format(int(binout[:8],2),int(binout[8:16],2),int(binout[16:24],2),int(binout[24:],2),int(binout[:8],2),int(binout[8:16],2),int(binout[16:24],2),int(binout[24:],2)))
print('\n'.join(output_m).format(mask[1],int(binmask[:8],2),int(binmask[8:16],2),int(binmask[16:24],2),int(binmask[24:],2),binmask[:8],binmask[8:16],binmask[16:24],binmask[24:]))
