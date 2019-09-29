import torch
import os
import glob




roberta = torch.hub.load('pytorch/fairseq', 'roberta.large.mnli')
roberta.eval()

original = [f for f in os.listdir('/home/mgnc2867/OpenNMT-py/data/originals') if os.path.isfile(os.path.join('/home/mgnc2867/OpenNMT-py/data/originals',f)) and f.endswith('.en.0.txt')]
simp = [f for f in os.listdir('/home/mgnc2867/OpenNMT-py/data/simples') if os.path.isfile(os.path.join('/home/mgnc2867/OpenNMT-py/data/simples',f)) and f.endswith('.en.3.txt')]
original.sort()
simp.sort()


e = open('notmatched1.txt', 'a')
d = open('emptyline1.txt','a')
g = open('same1.txt', 'a')
h = open('original1.txt', 'a')
i = open('simple1.txt', 'a')
j = open('contradiction1.txt', 'a')
k = open('entailment1.txt', 'a')


#l = open('trainori1.txt', 'w')
#m = open('trainsim1.txt', 'w')
#n = open('traincon1.txt', 'w')
#o = open('trainent1.txt', 'w')
#p = open('trainsame1.txt','w')
#q = open('traintoobig1.txt','w')
#r = open('trainemptyline1.txt','w')




original_array =[]
with open('/home/mgnc2867/OpenNMT-py/data/train.en', 'r') as myfile:
	for line in myfile:
		original_array.append(line)
original_array[:] = [line for line in original_array if line != '\n']


simple_array = []
with open('/home/mgnc2867/OpenNMT-py/data/train.sen', 'r') as myfile1:
	for line in myfile1:
		simple_array.append(line)
simple_array[:] = [line for line in simple_array if line !='\n']
	

def cycle_through(filename,filename1):
	f = open('/home/mgnc2867/OpenNMT-py/data/originals/'+filename, 'r')
	f1 = open('/home/mgnc2867/OpenNMT-py/data/simples/'+filename1, 'r')
	lines= f.readlines()
	simples = f1.readlines()
	lines[:] = [line for line in lines if line !='\n']
	simples[:] = [simple for simple in simples if simple !='\n']
	for line in lines:
		original.append(line)
	for simple in simples:
		simp.append(simple)
	per = int((b/len(original))*100)
	print('File is  - '+str(per)+'%')
	c = 0
	for line,line1 in zip(lines,simples):
		perc = int((c/len(lines))*100)
		tokens = roberta.encode(line,line1)
		prediction = roberta.predict('mnli',tokens).argmax().item()
		c += 1
		if line == line1:
			g.write(line+'\n'+line1+'\n'+'\n')
			print("Matched - "+ str(perc)+'%')
			
		elif line == '\n' or line == '':
			d.write(line1+'\n'+line2+'\n'+'\n')
			print("Empty line - " + str(perc)+'%')	
			
		elif line1 == '\n' or line1 == '':
			d.write(line1+'\n'+line2+'\n'+'\n')
			print("Empty line1 - " + str(perc)+'%')	
			
		elif prediction == 2 and line != line1 and line !='\n' and line1 != '\n' and line != '' and line1 != '':
			h.write(line+'\n')
			i.write(line1+'\n')
			print('Simplified - '+ str(perc)+'%')
			
		elif prediction == 0 and line != line1 and line !='\n' and line1 != '\n' and line != '' and line1 != '':
			j.write(line+'\n'+line1+'\n'+'\n')
			print('Contradict - '+ str(perc)+'%')
			
		else:
			k.write(line+'\n'+line1+'\n'+'\n')
			print('Entailment - '+ str(perc)+'%')
			

			


def original_cycle(line1, line2):
			tokens = roberta.encode(line1, line2)
			if len(tokens) < 512: 
				prediction = roberta.predict('mnli',tokens).argmax().item()
				percent = int((a/len(original_array))*100)
				if line1 == line2:
					p.write(line1+'\n'+line2 +'\n'+'\n')
					if percent == 100:
						print('\n'+'\n'+'\n'+'\n'+'FINISHED!'+'\n'+'\n'+'\n'+'\n')
					else:
						print("Matched - "+str(percent)+'%')
				elif line1 == '\n':
					r.write(line1+'\n'+ line2+ '\n'+'\n')
					print('Line1 Empty - ' +str(percent) +'%')
				elif line2 == '\n':
					r.write(line1+'\n'+line2+'\n'+'\n')
					print('Line2 Empty - ' +str(percent) +'%')
				elif prediction == 2 and line1 != line2 :
					l.write(line1+'\n')
					m.write(line2+'\n')
					if percent == 100:
						print('\n'+'\n'+'\n'+'\n'+'FINISHED!'+'\n'+'\n'+'\n'+'\n')
					else:
						print("Simplified - "+str(percent)+'%')
				elif prediction == 0:
					n.write(line1+'\n'+line2+'\n'+'\n')
					if percent == 100:
						print('\n'+'\n'+'\n'+'\n'+'FINISHED!'+'\n'+'\n'+'\n'+'\n')
					else:
						print("Contradict - "+str(percent)+'%')
				
				else:
					o.write(line1+'\n'+line2+'\n'+'\n')
					if percent == 100:
						print('\n'+'\n'+'\n'+'\n'+'FINISHED!'+'\n'+'\n'+'\n'+'\n')
					else:
						print("Entailment - "+str(percent)+'%')
			else:
				q.write('\n'+line1+'\n'+line2+'\n'+'\n')
				print("Too big - written to file")

			
'''
a = 0
for line1, line2 in zip(original_array, simple_array):
	original_cycle(line1,line2)
	a += 1
'''		
	
b = 0
for filename,filename1 in zip(original,simp):
	split = filename.split(".")
	split1 = filename1.split(".")
	if split[0] == split1[0]:
		print(filename+'\n'+filename1+'\n')
		cycle_through(filename,filename1)
		b += 1
	else:
		print('\n'+'File Names not matched'+'\n')
		print(filename+'\n'+filename1+'\n')
		e.write(filename+'\n'+filename1+'\n'+'\n')
		b += 1





e.close()
f.close()
g.close()
h.close()
i.close()
j.close()
k.close()

#l.close()
#m.close()
#n.close()
#o.close()
#p.close()
#q.close()
#r.close()































'''
with torch.no_grad():
	for file1, file2 in zip(original,simple):
		for line1,line2 in zip(file1, file2):
			tokens = robert.encode(line1,line2)
			prediction = roberta.predict('mnli', tokens).argmax().item()
			if prediction == 1:
				f.write('\n'+original)
				g.write('\n'+simple)
			elif prediction == 0:
				h.write(original+'\n'+simple+'\n'+'\n')
			else:
				i.write(original+'\n'+simple+'\n'+'\n')

'''
