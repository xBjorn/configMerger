"""Written to merge two CFG of a different game with the same game-engine(commands), with eachother"""
"""Comparing equivalent commands in the Quake CFG to the Sof2 CFG, and adding the Quake commands to the new config"""
"""Cuz I wanted rapha's(quake pro player) settings in sof, the easy way."""

#Written by Bjorn cuz I aint doing that by hand. Thats too much of a hussle. And we aint about that life.
#Soldier OF Fortune 2
#sof2mp

quakeCfg = input("Quake CFG 1:\n")
sofCfg = input("SoF2 CFG 2:\n")
overwrittenCfg = input("Name crafted CFG:\n")

a = open(quakeCfg, 'r')
b = open(sofCfg, 'r')
c = open(overwrittenCfg, 'w')

l1 = a.readlines()
l2 = b.readlines()

#Leaves some commands untouched. Personal preference. Adjust if needed.
bad_cmds = ['bind s_volume','bind space','bind ctrl','bind q','bind e','fullscreen','crosshair','bind h', 'bind r','bind a','bind w','bind s','bind d','r_subdivisions','seta name','unbindall','r_mode','r_customheight','r_customwidth','r_displayrefresh','bind mouse1','bind mouse2']

for x in l1:        
	for y in l2:
		if x.split('"')[0] == y.split('"')[0]:
			if not any(bad_cmd in x.lower() for bad_cmd in bad_cmds):
				c.write(x)
c.close()




		



