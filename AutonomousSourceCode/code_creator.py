#!/usr/bin/python
__author__ = 'Erick Miller for Stanford CS221'

import os
import re
import ast
import sys
import uuid
import copy
import json
import astor
import time
import random
import string
import autopep8
import itertools
import subprocess
import numpy as np
from redbaron import RedBaron
from collections import OrderedDict
from difflib import SequenceMatcher
from editdistance import eval as LevenshteinDistance
import math
from math import *

import astutils
from astutils import *
from timeout import timeout
import features




############################################################
############################################################
#
# SORT
#

#
#
# Definition = '"def sort( seq ):"'
#
# CorrectAnswer = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'm', 'n', 'o', 'p', 'qq', 'z']
#
# InputExample= ['ll', 'gg', 'aa', 'jj', 'cc', 'ee', 'hh', 'dd', 'p', 'o', 'm', 'bb', 'kk', 'ff', 'n', 'ii', 'z', 'qq']
#
# TrainedWeights = "cv/lm_lstm_epoch50.00_0.9887.t7"
#
# temp_dir = "/tmp/"
#

############################################################
############################################################


#
#
# Definition = '"def square_root( num ):"'
#
# InputExample= 262144
#
# CorrectAnswer = 512
#
# TrainedWeights = "cv/lm_lstm_epoch50.00_0.6677.t7"
#
# temp_dir = "/tmp/"
#
#
#
# ###########################################################
# ###########################################################
#
#
#
# Definition = '"def squared( num ):"'
#
# InputExample= 512
#
# CorrectAnswer = 262144
#
# TrainedWeights = "cv/lm_lstm_epoch50.00_0.6677.t7"
#
# temp_dir = "/tmp/"
#
#
# ###########################################################
# ###########################################################
#
#
#
#
# Definition = '"def half( num ):"'
#
# InputExample= 512
#
# CorrectAnswer = 256
#
# TrainedWeights = "cv/lm_lstm_epoch50.00_0.6677.t7"
#
# temp_dir = "/tmp/"






############################################################
############################################################


Definition = '"def double( num ):"'

InputExample= 512

CorrectAnswer = 1024

TrainedWeights = "cv/lm_lstm_epoch50.00_0.6677.t7"


temp_dir = "/tmp/"



#random.sample(CorrectAnswer , len(CorrectAnswer ))





class RewriteCode(ast.NodeTransformer):
    def __init__(self, oldCode, newCode):
        self.oldCode = oldCode
        self.newCode = newCode
        self.phi = features.Features()

    def visit_Call(self, node):
        if isinstance( node, ast.Call):
            source_code = astor.to_source(node)
        counter=0
        for origKw, mutantKw in zip(self.oldCode , self.newCode):
            if( origKw in source_code ):
                old = re.escape(origKw)
                source_code = self.phi.stripEmptyTokens( re.sub( r''+old, mutantKw, source_code ) )
                counter = counter + 1
                if( counter == len(self.newCode)):
                    try:
                        newNode = ast.parse( source_code )
                        for new in ast.walk(newNode):
                            if isinstance( new, ast.Call):
                                return ast.copy_location(new, node)
                    except Exception as e:
                        pass
                        return node
            else:
                return node
        return node



def cartesianProduct(n, seq):
    for perm in itertools.product(seq, repeat=n):
        yield perm


def KnuthShuffledPermutations( variables, doElimination=True ):

    def permutations( seq ):
        result=[]
        for perms in itertools.permutations(seq):
            result.append( list( perms ) )
        return result

    varPermutations = permutations( variables )

    variableEliminations = []
    if( doElimination ):
        for permutation in varPermutations:
            for i in range( len(permutation) ):
                eliminationSequence = ['']*(i+1)+permutation[(i+1):]
                if not eliminationSequence in variableEliminations:
                    variableEliminations.append( eliminationSequence )

    varCombinatorics =  varPermutations + variableEliminations
    np.random.shuffle( varCombinatorics )
    return varCombinatorics


def varMutationsIter(keywordAstMutations, variableCombinations):
    for kwrd in keywordAstMutations:
        for _ in variableCombinations:
            yield kwrd


def varComboIter(keywordAstMutations, variableCombinations):
    for _ in keywordAstMutations:
        for var in variableCombinations:
            yield var



validFunctions = []
possibleFunctions = []

for t in np.arange( 0.1, 1, 0.1):

    print "\n\n******************************\nSAMPLING NEURAL NETWORK\n********************************\n\n"
    # Uniformly sample the pre-trained neural network:
    #
    cmd = 'th sample.lua {} -primetext {} -length 4000 -temperature {}  2>&1'.format( TrainedWeights, Definition, t )
    output = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd ), shell = True )
    output = "".join([s for s in output.splitlines(True) if s.strip("\r\n")])

    # print "\n\n******************************\nSAMPLING NEON\n********************************\n\n"
    # #
    # # Random samples using second RNN
    # #
    # cmd2 = 'python code_gen_lstm.py -st {} -ns 3000 2>&1'.format( Definition )
    # output2 = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd2 ), shell = True )
    # output2 = "".join([s for s in output2.splitlines(True) if s.strip("\r\n")])
    #
    # print "\n\n******************************\nCOMBINING\n********************************\n\n"
    # output = output + "\n" + output2

    print "\n\n******************************\nPROCESSING\n********************************\n\n"

    phi = features.Features()
    functions = phi.parseFunctions(output)
    possibleFunctions = possibleFunctions + functions

    print "\n\n******************************\nTURNING INTO ASTs\n********************************\n\n"

    f=-1
    while f <= len(functions) :
        f = f+1
        try:
            fixedCode = autopep8.fix_code(functions[f])
            ASTree = ast.parse( fixedCode )
            code = astor.to_source( ASTree ).rstrip()
            validFunctions.append( code )
        except:
            pass
            continue
    validFunctions = list(OrderedDict.fromkeys(validFunctions))



if not validFunctions or f == -1:
    print "Result: (sorry) NO VALID FUNCTIONS COULD BE CONSTRUCTED."
    exit()



print "\n\nVALID FUNCTIONS BUILT BY NEURAL NETWORK! NOW, AST COMBINATORIAL FORESTS... "



scoredFunctions = OrderedDict()

for code in validFunctions:

    # start the cross-over and mutation process with static analysis heuristic using pylint

    # file_name = temp_dir + str(uuid.uuid4()) + "__" + re.sub('[^0-9a-zA-Z]+', '_', code.split("\n")[0]) +".py"
    #
    # f = open(file_name, 'w')
    # f.write(code)
    # f.close()
    #
    # Estring = "E:"
    # E = '"'+Estring+'"'
    # rating_string = "code has been rated at"
    # rating_filter = '"'+rating_string+'"'
    # cmd = 'pylint {} | grep -e {} -e {} 2>&1'.format( file_name, E, rating_filter )
    #
    # output = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd ), shell = True )
    # output = "".join([s for s in output.splitlines(True) if s.strip("\r\n")])
    #
    # results = output.split("\n")
    #
    # score = 0.0
    # Errors=[]
    # for result in results:
    #     if rating_string in result:
    #         score = score + float(re.sub( "/.*", "", re.sub(".*"+rating_string+" ", "", result)))
    #
    #     elif result.startswith(Estring):
    #         if( "syntax-error" in result ):
    #             score = -9999999.0 + score
    #
    #         Errors.append( re.sub("^"+Estring, "", result) )
    #         print "ERROR FOUND!"
    #         #score = -1.0 + score
    #
    # print Errors
    # scoredFunctions[ code ] = [ score, Errors ]


    scoredFunctions[ code ] =  [ len(code), "" ]


import operator


scoredFunctions = sorted( scoredFunctions.items(), key=operator.itemgetter(1))

# for code, score_error in scoredFunctions:
#     print "\n\n"
#     print len(code)
#     print code
#     print "\n\n"






for code, score_error in scoredFunctions:
    print "\n\n**********************************************\n\n"
    print code
    print "\n\n**********************************************\n\n"

#exit()





validWorkingFunctions = OrderedDict()
insufficientFunctions = OrderedDict()
phi = features.Features()
singleVariation = []

for code, score_error in scoredFunctions:

    # print "FUNCTION: \n"
    # print code
    # print "\nSCORE: ", score_error[0]
    # if len(score_error[1]):
    #     print "\nERRORS: \n"
    #     print score_error[1]
    # print "\n\n********\n\n"


    ASTree = ast.parse( code )


    functionNames = []
    functionNodes = []
    for node in ast.walk(ASTree):
        if isinstance( node, ast.FunctionDef):
            if node.name in dir(__builtins__) :
                while node.name in dir(__builtins__) :
                    node.name = node.name+random.choice(string.letters)
            functionNames.append( node.name )
            functionNodes.append( node )

    funcCallNodes = []
    funcCallNames = []
    keywordNames = []
    keywordNodes = []
    excludeNames = []
    for node in ast.walk(ASTree):
        if isinstance( node, ast.Call):
            funcCallNodes.append( node )

            #
            # booom, this guy does some heavy lifting:
            #
            deconstructed = deconstructAST( astor.to_source(node) )
            #
            ###

            for pieces in deconstructed:
                funcCallNames.append( pieces.func )
                if len(pieces.keywords):
                    for key in pieces.keywords:
                        keywordNames.append( key+"="+str(pieces.keywords[key]) )
                        excludeNames.append( str(pieces.keywords[key]) )
                        excludeNames.append( key )

    variableNodes = []
    variableNames = []
    for node in ast.walk(ASTree):
        if isinstance(node, ast.Name ) and \
                not node.id in (functionNames + funcCallNames + excludeNames ):
                variableNodes.append( node )
                variableNames.append( node.id )


    m_x_n = 6
    if( len(variableNames) > m_x_n-1
        or len(keywordNames) > m_x_n-1
        or len(funcCallNames) > m_x_n-1
        or len(functionNames) > 1 ):

        print "\nInfo: Logic sequences larger than ", m_x_n, " steps and multiple functions are not currently supported."
        print "Info: Skipping combination sequence mutation testing for:"
        print code, "\n"
        singleVariation.append(code)
        continue

    print "\n\n*****************************************************************************\n\n"
    print "\nFunction Name: "
    for name in functionNames:
        print "\t",name

    print "\nFunction Calls: "
    for name in funcCallNames:
        print "\t",name

    print "\nVariable Names: "
    for name in variableNames:
        print "\t",name

    print "\nNot Variable Names:"
    for name in excludeNames:
        print "\t",name

    print "\nKeywords: "
    for name in keywordNames:
        print "\t",name

    print "SOURCE CODE BEFORE RECOMBINATING: \n"
    print astor.to_source( ASTree )
    print "\n\n*****************************************************************************\n\n"

    #print "Random permutation: "
    #print np.random.permutation( variableNames )

    withElimination = variableNames+['']

    variableCombinations = cartesianProduct( len(variableNames), withElimination  )

    keywordCombinations = KnuthShuffledPermutations( keywordNames )

    keywordAstMutations = [ copy.deepcopy( ASTree ) for k in keywordCombinations ]
    for kwrds, astMutant in zip(keywordCombinations, keywordAstMutations):
            rewriter = RewriteCode(keywordNames, kwrds)
            rewriter.visit(astMutant)

    keyWordMutateSource = list(OrderedDict.fromkeys([ astor.to_source(kwmut) for kwmut in keywordAstMutations ]))
    keywordAstMutations = []
    for kwmut in keyWordMutateSource:
        try:
            keywordAstMutations.append( ast.parse(kwmut) )
        except:
            pass

    varAstMutations = varMutationsIter(keywordAstMutations, variableCombinations)

    varCombos = varComboIter(keywordAstMutations, variableCombinations)

    allMutatedVariations=[]
    exclude = functionNames + funcCallNames + excludeNames
    for vCombo, vMutant in itertools.izip(varCombos, varAstMutations):
        vcIter = iter(vCombo)
        for node in ast.walk(vMutant):
            if isinstance(node, ast.Name ) and not node.id in exclude:
                value = vcIter.next()
                node.id = value
        try:
            allMutatedVariations.append( phi.stripEmptyTokens( astor.to_source( vMutant ).rstrip() ) )
            astor.to_source( newVarTree ).rstrip()
        except:
            pass


    allMutatedVariations = singleVariation + allMutatedVariations + keyWordMutateSource
    allMutatedVariations = list(OrderedDict.fromkeys(allMutatedVariations))

    num=0

    skip_infinity = 0
    infinite_function = ""
    infinite_bound = 10 # in seconds

    for mutatedFunction in allMutatedVariations:

            success = False
            didCompile = False
            didExec = False

            try:
                codeobj = compile(mutatedFunction, '__', 'exec')
                didCompile = True
            except:
                pass
                didCompile = False

            if didCompile:
                try:
                    exec(codeobj)
                    didExec = True
                except:
                    pass
                    didExec = False

                if didCompile and didExec :
                    try:
                        red = RedBaron(mutatedFunction)
                        functor = red.find('DefNode').name

                        if functor == infinite_function and skip_infinity > 1 :
                            print "SKIPPING POTENTIAL INFINITE FUNCTION... i.e.  while True: print 'infinity'"
                            print "This branch of code is timing out... skipping further mutations:\n"
                            print mutatedFunction
                            continue

                        if skip_infinity > 1 and functor != infinite_function :
                            infinite_function = ""
                            skip_infinity = 0

                        #
                        # print "\n\n*************************************************\n\n"
                        # print "FOR THIS CODE:\n"
                        # print mutatedFunction
                        # print "\n\n*************************************************\n\n"
                        #

                        @timeout(infinite_bound)
                        def TreeHealthError( func, correct, incorrect  ):

                            # redirect stdout to suppress print statements
                            orig_stdout = sys.stdout
                            f = open(os.devnull, 'w')
                            sys.stdout = f

                            RetVal = False

                            try:
                                evalString = func+'('+str(json.dumps(incorrect))+')'

                                # print "Running EVAL on:"
                                # print evalString

                                result = eval(evalString)

                                corr = str(json.dumps(correct))
                                res = str(json.dumps(result))

                                LevenshteinDist = float( LevenshteinDistance( corr, res) )
                                RatcliffObrshlp = 10.0 * (1.0 - SequenceMatcher(None, corr, res).ratio())
                                ErrorHeuristic = RatcliffObrshlp + LevenshteinDist

                                if( result == correct ):
                                    RetVal = [True, ErrorHeuristic]
                                else:
                                    RetVal = [False, ErrorHeuristic ]

                            except Exception:
                                #print e
                                pass
                                RetVal = False

                            sys.stdout = orig_stdout

                            return RetVal


                        startTime = time.time()
                        #print "START TIME: ", startTime
                        # primary heuristic
                        #
                        success = TreeHealthError( functor, CorrectAnswer, InputExample)

                        #print "RESULT FROM TEST: ", success

                        finishTime = time.time() - startTime
                        if( finishTime >= (float(infinite_bound) - .0001) ):
                            print "\n\n*************************FUNCTION: ",functor ," RAN LONGER THAN EXPECTED:", finishTime ," seconds. SKIPPING\n***********************************\n\n"
                            if infinite_function != functor:
                                skip_infinity = 1
                            skip_infinity = skip_infinity + 1
                            infinite_function = functor

                        #print "FINISH TIME: ", finishTime

                        success[1] = success[1] + float(finishTime)

                        #print "UPDATED SUCCESSS: ", success

                        # print "\n\n*************************************************\n\n"
                        # print "FOR THIS CODE:\n"
                        # print mutatedFunction
                        # print "\n\n*************************************************\n\n"

                        del codeobj

                    except Exception:
                        #print e
                        pass
                        success = False

                if( success != False ):
                    if( success[0] == True ):
                        print "A VALID FUNCTION WAS CREATED THAT passed the Test()! Cool! "
                        print "\n*********************************************************************\n"
                        print "\n*********************************************************************\n"
                        print "\n*********************************************************************\n"
                        print "\n*********************************************************************\n"
                        print "\n\nHere is the working Code and it's Abstract Syntax Tree! \n\n"

                        ASTpassed = ast.parse(mutatedFunction)
                        validToCode = astor.to_source(ASTpassed).rstrip()

                        validWorkingFunctions[ validToCode ] = success[1] #+ float(len(validToCode))

                        print validToCode,"\n\n"

                        astPrint = astutils.AstPrettyPrinter()
                        print astPrint.pprint( ASTpassed )

                    elif( success[0] == False ):
                        ASTpassed = ast.parse(mutatedFunction)
                        valideButInsufficient = astor.to_source(ASTpassed).rstrip()
                        insufficientFunctions[ valideButInsufficient ] = success[1]



insufficientFunctions = sorted( insufficientFunctions.items(), key=operator.itemgetter(1))
validWorkingFunctions = sorted( validWorkingFunctions.items(), key=operator.itemgetter(1))

#validWorkingFunctions = list(OrderedDict.fromkeys(validWorkingFunctions))

possibleFunctions = list(OrderedDict.fromkeys(possibleFunctions))

print "\nSummary: generated total of ", len(possibleFunctions), " candidate functions, and ", len(validFunctions), " were valid python code\n"


print "Summary: of all the isufficient (but valid mutations) the generator made: ", len(insufficientFunctions), " here: "

counter = 0
random.shuffle( insufficientFunctions )
for insfficient, error in insufficientFunctions:
    #if( counter < 10):
    print "\n", insfficient, "\n[AN ERROR OF: ", error,"]"
    print "\n"
    # else:
    #     break
    # counter=counter+1

print "Summary: of all the valid code, the Automatous Code Ai constructed: ", len(validWorkingFunctions), " valid Tested functions, and here they are: "

for workingFunction, error in validWorkingFunctions:
    print "\n", workingFunction, "\n[Has an error of: ", error,"]"
    print "\n"

