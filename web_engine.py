import matplotlib
matplotlib.use('Agg')
import spice

netlist="""
*acMOS

V1 1 0 1.8 sin 0 0 100000MEG 0
R1 2 3 200


V2 3 0 3
C1 2 0 10p
MN1 2 1 0 2 1

.AC DEC 20 1MEG 1000MEG
.END
"""
spice.parse(netlist)