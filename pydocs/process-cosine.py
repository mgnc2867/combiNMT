import csv

e = open('/home/mgnc2867/OpenNMT-py/data/edited-data/trainori-processed995.txt','w+')
g = open('/home/mgnc2867/OpenNMT-py/data/edited-data/trainsim-processed995.txt','w+')
h = open('/home/mgnc2867/OpenNMT-py/data/too-similar995.txt','a')

with open('/home/mgnc2867/OpenNMT-py/data/train-similarity.csv','r') as sim:
	csv_reader = csv.reader(sim,delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
			continue
		else:
			sim = float(row[2])
			if line_count != 0 and sim >= 0.995:
				h.write(row[0])
				h.write(row[1])
			else:
				e.write(row[0])
				g.write(row[1])
