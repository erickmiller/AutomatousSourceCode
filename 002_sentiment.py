#!/usr/bin/python

import random
import collections
import math
import sys
from collections import Counter
from util import *

############################################################
# Problem 3: binary classification
############################################################

############################################################
# Problem 3a: feature extraction
import re, string

def extractWordFeatures(x):
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    featurevect = collections.OrderedDict()
    words = x.split()
    filteredWords = []
    for word in words:
        fixedWord = re.sub('[\W_]+', '', word )
        if(len(fixedWord)):
            filteredWords.append(fixedWord)

    random.shuffle(filteredWords)
    for item in collections.Counter(filteredWords).most_common() :
        featurevect[ item[0]  ] = item[1]

    return featurevect
    # END_YOUR_CODE


############################################################
# Problem 3b: stochastic gradient descent


def learnPredictor(trainExamples, testExamples, featureExtractor):
    '''
    Given |trainExamples| and |testExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of iterations to
    train |numIters|, return the weight vector (sparse feature vector) learned.

    You should implement stochastic gradient descent.

    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and testExamples
    to see how you're doing as you learn after each iteration.
    numIters refers to a variable you need to declare. It is not passed in.
    '''
    weights = {}  # feature => weight

    AllPoints = trainExamples
    points = []
    for point in AllPoints:
        featurePoints = featureExtractor(point[0])
        featureValue = float(point[1])
        addthis = ( featurePoints , featureValue )
        points.append( addthis )
    random.shuffle(points)

    def scale( val, vector ):
        newvector = collections.OrderedDict()
        itemsin = vector.items()
        total = sum(vector.values(), 0.0)
        for f, v in itemsin:
            newvector[f] = ( val * float( v ) ) / float(total) #normalize
            #newvector[f] =  val * float( v )
        return newvector

    def stochasticGradientDescent( dvHingeLoss, n  ):
        w = {}
        numIters = 20
        eta = 0.15
        for t in  range(numIters):
            for i in range(n):
                gradient = dvHingeLoss(w, i)
                if( gradient != 0  ): #found minimum?
                    increment(w, -eta, gradient )
        return  w

    def dvHingeLoss(w, i):
        x, y = points[i]
        v_i = y * dotProduct( x, w )
        return 0 if v_i >= 1 else scale(-y, x)

    weights = stochasticGradientDescent( dvHingeLoss, len(points) )
    return weights



trainExamples = readExamples('polarity.train')
devExamples = readExamples('polarity.dev')
featureExtractor = extractWordFeatures
weights = learnPredictor(trainExamples, devExamples, featureExtractor)
outputWeights(weights, 'weights')
outputErrorAnalysis(devExamples, featureExtractor, weights, 'error-analysis')  # Use this to debug
trainError = evaluatePredictor(trainExamples, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
devError = evaluatePredictor(devExamples, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
print "Official: train error = %s, dev error = %s" % (trainError, devError)
print "Train error should be less than: 0.08 and ...IT IS ACTUALLY: " +  str(trainError)
print "Dev error should be less than: 0.30 and ...IT IS ACTUALLY: " +  str(devError)





############################################################
# Problem 3c: generate test case

def generateDataset(numExamples, weights):
    '''
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    '''
    random.seed(42)
    # Return a single example (phi(x), y).
    # phi(x) should be a dict whose keys are a subset of the keys in weights
    # and values can be anything (randomize!) with a nonzero score under the given weight vector.
    # y should be 1 or -1 as classified by the weight vector.
    def generateExample():
        key = random.sample(weights, 1)
        value = weights[key[0]]
        if value == 0:  value = random.uniform(0.1, 1.0)
        phi = { key[0] : ( value * random.uniform(0.1, 10) ) }
        y = weights[key[0]]
        return (phi, y)
    return [generateExample() for _ in range(numExamples)]




############################################################
# Problem 3f: character features

def extractCharacterFeatures(n):
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    '''
    def extract(x):
        letters = ''.join(x.split())
        ngrams = zip(*[letters[i:] for i in range(n)])
        for i in range(len(ngrams)):  ngrams[i] = ''.join(ngrams[i])
        featurevect = collections.OrderedDict()
        for item in collections.Counter(ngrams).most_common() :
            featurevect[ item[0] ] = item[1]
        return featurevect

    return extract


#
# trainExamples = readExamples('polarity.train')
# devExamples = readExamples('polarity.dev')
# featureExtractor = extractCharacterFeatures(5)
# weights = learnPredictor(trainExamples, devExamples, featureExtractor)
# outputWeights(weights, 'weights')
# outputErrorAnalysis(devExamples, featureExtractor, weights, 'error-analysis')  # Use this to debug
# trainError = evaluatePredictor(trainExamples, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
# devError = evaluatePredictor(devExamples, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
# print "Official: train error = %s, dev error = %s" % (trainError, devError)
# print "Train error should be less than: 0.08 and ...IT IS ACTUALLY: " +  str(trainError)
# print "Dev error should be less than: 0.30 and ...IT IS ACTUALLY: " +  str(devError)
#





############################################################
# Problem 3h: extra credit features

def extractExtraCreditFeatures(x):
    # BEGIN_YOUR_CODE (around 1 line of code expected)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE



############################################################
# Problem 4: k-means
############################################################

def kmeans(examples, K, maxIters):
    '''
    examples: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxIters: maximum number of iterations to run for (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments, (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    '''

    def distanceSquared(a, b):
       return sum((float(a[k]) - float(b[k]))**2.0 for k in a.keys())

    n = len(examples)
    points = list()
    for example in examples:
        points.append( collections.Counter( example ) )
    mu = [points[random.randint(0,n-1)] for k in range(K)]
    assignments = [None] * n
    oldTotalCost = None
    totalCost = 0.0
    totalIters = 0
    while True:
        totalCost = 0.0
        for i, x in enumerate(points):
            cost, assignments[i] = min(( (distanceSquared(x, mu[k])), k) for k in range(K))
            totalCost += cost
        if totalCost == oldTotalCost or maxIters == totalIters:
            break

        oldTotalCost = totalCost
        totalIters = totalIters + 1

        for k in range(K):
            myPoints = [x for i, x in enumerate(points) if assignments[i] == k]
            if len(myPoints) > 0:
                centerPoint, newMu = Counter(), Counter()
                for i in range(len(myPoints)):
                    for key in myPoints[i]:
                        centerPoint[key] = float( myPoints[i][key] ) + float( centerPoint[key] )
                for key in centerPoint:
                    newMu[key] = centerPoint[key] / float( len(myPoints) )
                mu[k]= newMu

    return mu, assignments, totalCost




#clusteringExamples = generateClusteringExamples(10, 1, 1)
#centers, assignments, totalCost = kmeans(clusteringExamples, 10, maxIters=10000)

#print clusteringExamples
#
# x1 = {0:0, 1:0}
# x2 = {0:0, 1:1}
# x3 = {0:0, 1:2}
# x4 = {0:0, 1:3}
# x5 = {0:0, 1:4}
# x6 = {0:0, 1:5}
# examples = [x1, x2, x3, x4, x5, x6]
# centers, assignments, totalCost = kmeans(examples, 2, maxIters=10)
#
# (there are two stable centroid locations)
# if round(totalCost, 3)==4 or round(totalCost, 3)==5.5 :
#     print "YES!!! PASSED FIRST TEST!"
# else:
#     print " Fail. Fix it."

#print "Centers:"
#for center in  centers:
#    print center
#print "Assignments:"
#print assignments
#print "Total Cost ROUNDED:"
#print round(totalCost, 3)









