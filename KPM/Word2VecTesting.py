# -*- coding: utf-8 -*-
from gensim.models import KeyedVectors
from gensim.models import Word2Vec
import logging, os


class MySentences(object):
    
    def __init__(self, dirname):
        self.dirname = dirname
        self.sent_list = []
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                l = line.split()
                for elem in l:
                    elem = elem.lower()
                self.sent_list.append(elem)

    def __iter__(self):
        for elem in self.sent_list:
            yield elem
                
    def __getitem__(self, key):
        return self.sent_list[key]
                
    def __len__(self):
        return(len(self.sent_list))

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = MySentences("../data/sentences")
print(len(sentences))
model = Word2Vec(sentences, workers = 3)
print("...beginning training...")
model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
model.save("word2vecmodel")
word_vectors = KeyedVectors.load("word2vecmodel")
word_vectors.wv.similarity('woman', 'man')
#min_count is minimimum appearances to be included (default = 5)
#size is the NN layers (default = 100)
#workers is number of cores (default = 1)
