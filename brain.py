import markovify
import nltk
from nltk.corpus import treebank
import glob, os
import time

os.chdir("library")
file1 = open('megacorpus.txt','a')

for file in glob.glob("*.txt"):
    with open(file) as f:
        text = f.read()
        file1.write(text+'\n')

file1.close();
file1  = open('megacorpus.txt')
text = file1.read()
text_model = markovify.Text(text, state_size=2)
file1.close()

start = time.time()
f = open('writings.txt','a')

for i in range(2500):
    text = text_model.make_sentence()
    f.write(text+'\n')

stop = time.time()
benchmark = str(stop - start)
f.write(benchmark)
f.close()