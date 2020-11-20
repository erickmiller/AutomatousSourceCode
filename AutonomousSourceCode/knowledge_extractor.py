#!/usr/bin/python
__author__ = 'Erick Miller for Stanford CS221'

import logging
import os.path
import sys

import gensim

import bz2

from gensim.corpora import Dictionary, HashDictionary, MmCorpus, WikiCorpus

from gensim.models import TfidfModel

import re

from gensim import corpora, models, similarities

import nltk
from nltk.corpus import stopwords


# DEFAULT_DICT_SIZE most frequent types are kept.
DEFAULT_DICT_SIZE = 5000
#
#

from bs4 import BeautifulSoup

import xml.etree.ElementTree as ET

#tree = ET.parse('file01.xml')

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



LDAFILE = '/tmp/LDA_saved_model-19'


if os.path.isfile(LDAFILE):

    print "\n\nLOADING FROM DISK YAY!\n\n"

    lda = gensim.models.ldamodel.LdaModel.load( LDAFILE )

    dictionary = Dictionary.load_from_text( '/tmp/test_V1.txt' )

    corpus = MmCorpus( '/tmp/test_V1.mm')


    index = similarities.MatrixSimilarity(lda[corpus])
    index.save("/tmp/simIndex.index")

    doc = "function sort list alphabetically return sorted list"

    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lda = lda[vec_bow]

    sims = index[vec_lda]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])

    print "\n\nSimilarities?!\n\n"
    print doc
    print "\n\n"


    for id, similar in sims[:10]:
       for cid, corp in corpus[ id ]:
           print dictionary[cid], " ", corp


#    print sims[0]

   # print sims

    print "\n\nTOPICS!\n\n"
    lda.print_topics(50)

 #   print lda.top_topics( corpus )



else:

#    tree = ET.parse('biggerChunk001.xml')

    tree = ET.parse('EvenBigger_01.xml')

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
        addThese = []
        if( words  ):
            for wrd in words.split():
                if len(wrd) > 2:
                    addThese.append( wrd )
            if len(addThese):
                postOnlyNoHtml.append( " ".join( addThese ) )

    s=set(stopwords.words('english'))

    texts = []
    my_file = open("/home/etron/CODE/project/knowledge_parsed.txt", "w")

    for txt in postOnlyNoHtml:
        fTxt = filter(lambda w: not w in s,txt.split())
        for tx in zip( fTxt[0::3], fTxt[1::3], fTxt[2::3] ):
            texts.append( [tx[0], tx[1], tx[2] ] )
            my_file.write( tx[0]+" "+tx[1]+" "+tx[2]+"\n" )


        #texts.append(  filter(lambda w: not w in s,txt.split()) )
        #texts.append( txt.split() )


    #print texts


    #
    # texts = [['human', 'interface', 'computer'],
    #          ['survey', 'user', 'computer', 'system', 'response', 'time'],
    #          ['eps', 'user', 'interface', 'system'],
    #          ['system', 'human', 'system', 'eps'],
    #          ['user', 'response', 'time'],
    #          ['trees'],
    #          ['graph', 'trees'],
    #          ['graph', 'minors', 'trees'],
    #          ['graph', 'minors', 'survey']]



    dictionary = corpora.Dictionary(texts)
    dictionary.save('/tmp/test_V1.dict') # save for later

    dictionary.filter_extremes(no_below=2, keep_n=DEFAULT_DICT_SIZE)

    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('/tmp/test_V1.mm', corpus) # store to disk, for later use

    #print(corpus)


    dictionary.save_as_text('/tmp/test_V1.txt')

    dictionary = Dictionary.load_from_text( '/tmp/test_V1.txt' )

    mm = MmCorpus( '/tmp/test_V1.mm')

    # lsi = gensim.models.lsimodel.LsiModel(corpus=mm, id2word=dictionary, num_topics=100)
    # print "\n\n\nRESULTS!\n"
    # lsi.print_topics(30)
    # print "\n"
    lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=dictionary, num_topics=50, update_every=0, passes=50)
    lda.save( LDAFILE  )

#    lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=dictionary, num_topics=100, update_every=1, chunksize=10000, passes=1)
    print "\n\n\nRESULTS!\n"
    lda.print_topics(50, 20)
    print "\n"




#
# wiki = WikiCorpus(   , lemmatize=lemmatize) # takes about 9h on a macbook pro, for 3.5m articles (june 2011)
#
# # only keep the most frequent words (out of total ~8.2m unique tokens)
# wiki.dictionary.filter_extremes(no_below=20, no_above=0.1, keep_n=DEFAULT_DICT_SIZE)
#
# # save dictionary and bag-of-words (term-document frequency matrix)
# MmCorpus.serialize(outp + '_bow.mm', wiki, progress_cnt=10000) # another ~9h
# wiki.dictionary.save_as_text(outp + '_wordids.txt.bz2')
#
# # load back the id->word mapping directly from file
# # this seems to save more memory, compared to keeping the wiki.dictionary object from above
# dictionary = Dictionary.load_from_text(outp + '_wordids.txt.bz2')
#
#
#
# # initialize corpus reader and word->id mapping
# mm = MmCorpus(outp + '_bow.mm')
#
# # build tfidf, ~50min
# tfidf = TfidfModel(mm, id2word=dictionary, normalize=True)
# tfidf.save(outp + '.tfidf_model')
#
# # save tfidf vectors in matrix market format
# # ~4h; result file is 15GB! bzip2'ed down to 4.5GB
# MmCorpus.serialize(outp + '_tfidf.mm', tfidf[mm], progress_cnt=10000)
#
# logger.info("finished running %s" % program)