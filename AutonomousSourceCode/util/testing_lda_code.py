import gensim

import logging
import os.path
import sys

import gensim

import bz2

from gensim.corpora import Dictionary, HashDictionary, MmCorpus, WikiCorpus

from gensim.models import TfidfModel

import re
import os.path

from gensim import corpora, models, similarities

import nltk
from nltk.corpus import stopwords

# first scanned for all distinct word types and the types that
# appear more than 10% of time are removed and from the rest, the
# DEFAULT_DICT_SIZE most frequent types are kept.
DEFAULT_DICT_SIZE = 1000
#
#

from bs4 import BeautifulSoup

import xml.etree.ElementTree as ET

#tree = ET.parse('file01.xml')

tree = ET.parse('biggerChunk001.xml')

root = tree.getroot()
htmlPosts = []
for row in root.findall('row'):
    if row.get('Tags') and row.get('Score'):
        if "python" in row.get('Tags').lower():
            if float( row.get('Score') ) >= 2.0 :
                htmlPosts.append( row.get('Body') )

postOnlyNoHtml = []
for htmPost in htmlPosts:
    soup = BeautifulSoup( htmPost )
    #words = " ".join( [ re.sub('[\W_]+', '', w.lower()) for w in soup.text.split() ]  )
    words = " ".join( [ re.sub('[^a-zA-Z]+', '', w.lower()) for w in soup.text.split() ]  )
    if( words  ):
        postOnlyNoHtml.append( " ".join( words.split() ) )

s=set(stopwords.words('english'))

texts = []

for txt in postOnlyNoHtml:
    texts.append(  filter(lambda w: not w in s,txt.split()) )

from nltk.data import find

#word2vec_sample = str(find('models/word2vec_sample/pruned.word2vec.txt'))

#model = gensim.models.Word2Vec.load_word2vec_format(word2vec_sample, binary=False)

savedModelFile = '/tmp/savedWordVecModel3'

if os.path.isfile(savedModelFile):
    model = gensim.models.Word2Vec.load(savedModelFile)
else:
    model = gensim.models.Word2Vec(texts , size=100, window=5, min_count=5, workers=4)
    model.save(savedModelFile)


print model.most_similar(positive=['sort'] )


import numpy as np

labels = []
count = 0
max_count = 1000
X = np.zeros(shape=(max_count,len(model['sort'])))

for term in model.vocab:
    X[count] = model[term]
    labels.append(term)
    count+= 1
    if count >= max_count: break

# It is recommended to use PCA first to reduce to ~50 dimensions
from sklearn.decomposition import PCA
pca = PCA(n_components=50)
X_50 = pca.fit_transform(X)

# Using TSNE to further reduce to 2 dimensions
from sklearn.manifold import TSNE
model_tsne = TSNE(n_components=2, random_state=0)
Y = model_tsne.fit_transform(X_50)

# Show the scatter plot
import matplotlib.pyplot as plt
plt.scatter(Y[:,0], Y[:,1], 20)

# Add labels
for label, x, y in zip(labels, Y[:, 0], Y[:, 1]):
    plt.annotate(label, xy = (x,y), xytext = (0, 0), textcoords = 'offset points', size = 10)

plt.show()
