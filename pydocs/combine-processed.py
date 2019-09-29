a = []
with open('/home/mgnc2867/OpenNMT-py/data/edited-data/newselaori-processed98.txt','r') as ori:
	for line in ori:
		a.append(line)
c =[]
with open('/home/mgnc2867/OpenNMT-py/data/edited-data/trainori-processed98.txt','r') as sim:
	for line in sim:
		c.append(line)
b= open('/home/mgnc2867/OpenNMT-py/data/edited-data/original98.txt','a')
a[:] = [f for f in a if f !='\n']
c[:] = [f for f in c if f !='\n']
b.write(str(a))
b.write(str(c))
