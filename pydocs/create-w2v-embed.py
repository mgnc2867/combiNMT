import re
import gensim
from gensim.models import Word2Vec

sentences = []
processed = []

with open('/home/mgnc2867/OpenNMT-py/data/edited-data/allori.txt','r') as abc:
	for line in abc:
		sentences.append(line)
sentences[:] = [f for f in sentences if f != '\n']


for line in sentences:
	line = line.lower()
	z = line.split()
	z[:] = [f for f in z if f != '']
	processed.append(z)
	
model = Word2Vec(processed, size=300, window=10, min_count=5, workers=4, iter=10)
model.wv.save_word2vec_format('combiNMT-original.txt', binary= False)
