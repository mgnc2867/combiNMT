import numpy
import csv

output= open('/home/mgnc2867/OpenNMT-py/data/newsela-similarity.csv','w+')
row = ['Original', ' Simplified', ' Similarity', ' Linear Algibra']
writer = csv.writer(output)
writer.writerow(row)
a = []
with open('/home/mgnc2867/OpenNMT-py/data/edited-data/original1.txt','r') as abc:
	for line in abc:
		a.append(line)



b = []
with open('/home/mgnc2867/OpenNMT-py/data/edited-data/simple1.txt','r') as bcd:
	for line in bcd:
		b.append(line)
index = 0
while index < len(b):
	line = a[index]
	line1 = b[index]
	vocab = set(line)
	vocab = vocab.union(set(line1))
	vocab = list(vocab)
	vA = numpy.zeros(len(vocab), dtype=float)
	vB = numpy.zeros(len(vocab), dtype=float)
	
	for w in line:
		i = vocab.index(w)
		vA[i] += 1
	for v in line1:
		i = vocab.index(v)
		vB[i] += 1
	sim = numpy.dot(vA,vB) / (numpy.sqrt(numpy.dot(vA,vA)) * numpy.sqrt(numpy.dot(vB,vB)))
	lin = numpy.dot(vA,vB) / (numpy.linalg.norm(vA)* numpy.linalg.norm(vB))
	row =[line,line1,str(sim),	str(lin)]
	writer.writerow(row)
	index +=1
	print(index)

