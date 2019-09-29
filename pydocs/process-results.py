import csv


eval1 =[]
eval2 =[]
eval3 =[]
eval4 =[]
eval5 =[]
total= 0
correct =0
results = open('/home/mgnc2867/OpenNMT-py/data/results995.csv', 'w')
writer = csv.writer(results)

with open('/home/mgnc2867/Downloads/results/1test-combiNMT995.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		eval1.append(row)
with open('/home/mgnc2867/Downloads/results/2-test-combiNMT995.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		eval2.append(row)
with open('/home/mgnc2867/Downloads/results/3-test-combiNMT995.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		eval3.append(row)
with open('/home/mgnc2867/Downloads/results/4-test-combiNMT995.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		eval4.append(row)
with open('/home/mgnc2867/Downloads/results/5-test-combiNMT995.csv') as csvfile:
	readcsv= csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		eval5.append(row)


count = 0
for row, row1, row2, row3, row4 in zip(eval1,eval2,eval3,eval4,eval5):
	if count ==0:
		line= [row[0],row[1],row[2],row[3]]
		writer.writerow(line)
		count +=1
	else:
		if row4[4] == 'FALSE':
			line = [row[0], row[1], ((int(row[2])+int(row1[2])+int(row2[2])+int(row3[2])+int(row4[2]))/5), ((int(row[3])+int(row1[3])+int(row2[3])+int(row3[3])+int(row4[3]))/5)]
			writer.writerow(line)
		else:
			line = [row[0], row[1], ((int(row[2])+int(row1[2])+int(row2[2])+int(row3[2])+10)/5), ((int(row[3])+int(row1[3])+int(row2[3])+int(row3[3])+10)/5)]
			
	
results.close()

print("Total number of changes: " + str(total))
print("Total correct changes: " + str(correct))
print("Percentage of correct changes: " + str(((correct/total)*100)) +"%")


	

eval11 =[]
eval21 =[]
eval31 =[]
eval41 =[]
eval51 =[]
total = 0
correct = 0
results = open('/home/mgnc2867/OpenNMT-py/data/results98.csv', 'w')
writer = csv.writer(results) 

with open('/home/mgnc2867/Downloads/results/1-test-combiNMT98.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		eval11.append(row)
with open('/home/mgnc2867/Downloads/results/2-test-combiNMT98.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		eval21.append(row)
with open('/home/mgnc2867/Downloads/results/3-test-combiNMT98.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		eval31.append(row)
with open('/home/mgnc2867/Downloads/results/4-test-combiNMT98.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		eval41.append(row)
with open('/home/mgnc2867/Downloads/results/5-test-combiNMT98.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		eval51.append(row)

count = 0
for row, row1, row2, row3, row4 in zip(alex1, leah1, lucy1, keri1, matt1):
	if count ==0:
		line = [row[0], row[1],row[2], row[3]]
		writer.writerow(line)
		count +=1
	else:
		if row4[4] == 'FALSE':
			line = [row[0], row[1], ((int(row[2])+int(row1[2])+int(row2[2])+int(row3[2])+int(row4[2]))/5), ((int(row[3])+int(row1[3])+int(row2[3])+int(row3[3])+int(row4[3]))/5)]
			writer.writerow(line)
		else:
			line = [row[0], row[1], ((int(row[2])+int(row1[2])+int(row2[2])+int(row3[2])+10)/5), ((int(row[3])+int(row1[3])+int(row2[3])+int(row3[3])+10)/5)]
			


print("Total number of changes: " + str(total))
print("Total correct changes: " + str(correct))
print("Percentage of correct changes: " + str(((correct/total)*100)) +"%")

results.close()
results = open('/home/mgnc2867/OpenNMT-py/data/results995.csv','a')
writer = csv.writer(results)
file =[]
number = 0.0
numbers = 0.0
with open('/home/mgnc2867/OpenNMT-py/data/results995.csv') as csvfile:
	readcsv = csv.reader(csvfile,delimiter=',')
	for row in readcsv:
		file.append(row)
count = 0
for row in file:
	if count == 0:
		count+=1
	else:
		number = number + float(row[2])
		numbers = numbers + float(row[3])


gram = number / len(file)-1
mean = numbers / len(file)-1
append = ['','',str(gram),str(mean)]
writer.writerow(append)

print('combiNMT995' + '\n'+ 'grammaticality mean: ' + str(gram) +'\n' + 'meaning preservation mean: ' + str(mean))

results.close()
results = open('/home/mgnc2867/OpenNMT-py/data/results98.csv','a')
writer = csv.writer(results)
file =[]
number = 0.0
numbers = 0.0
with open('/home/mgnc2867/OpenNMT-py/data/results98.csv') as csvfile:
	readcsv = csv.reader(csvfile,delimiter=',')
	for row in readcsv:
		file.append(row)
count = 0
for row in file:
	if count == 0:
		count+=1
	else:
		number = number + float(row[2])
		numbers = numbers + float(row[3])


gram = number / len(file) -1
mean = numbers / len(file) -1

append = ['','',str(gram),str(mean)]
writer.writerow(append)


print('combiNMT98' + '\n'+ 'grammaticality mean: ' + str(gram) +'\n' + 'meaning preservation mean: ' + str(mean))

