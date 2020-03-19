#!/bin/sh
## The default configuration incase you want to revert
#  P0 - Enabled - FID = 78 (120) - DID = 8 - VID = 3A - Ratio = 30.00 - vCore = 1.18750
#  P1 - Enabled - FID = 87 (135) - DID = A - VID = 50 - Ratio = 27.00 - vCore = 1.05000
#  P2 - Enabled - FID = 7C (124) - DID = 10 - VID = 6C - Ratio = 15.50 - vCore = 0.87500

## P0 = 3.375GHz, 1.05000v
zenstates.py -p 0 -f 87 -d A -v 50

## P1 = 3.375GHz, 1.05000v
zenstates.py -p 1 -f 7C -d 10 -v 6C

## P2 = 3.000GHz, 1.18750v
zenstates.py -p 2 -f 78 -d 8 -v 3A

## List the result.
zenstates.py -l                                                                                                                                                                                       
