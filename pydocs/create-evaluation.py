import random
import csv
numbers= []
csvFile = open('test-combiNMT98.csv', 'w')
writer = csv.writer(csvFile)
row = ["Original", "Simplified", "Grammar", "Meaning"]
writer.writerow(row)
original_array =[]

with open('/home/mgnc2867/OpenNMT-py/data/test.en', 'r') as myfile:
	for line in myfile:
		original_array.append(line)
original_array[:] = [f for f in original_array if f != '\n']
		
simple_array = []
with open('/home/mgnc2867/OpenNMT-py/data/test-combiNMT98.txt', 'r') as myfile1:
	for line in myfile1:
		simple_array.append(line)
simple_array[:] = [f for f in simple_array if f != '\n']
	


for x in range(120):
	number = random.randint(0,len(original_array))
	numbers.append(number)

a=120
while a <= 240:
		a+=1
		line1 = original_array[a]
		line2 = simple_array[a]
		row = [line1, line2,"",""]
		writer.writerow(row)


csvFile.close()
