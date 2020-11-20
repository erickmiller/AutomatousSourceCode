import shell
import util
import wordsegUtil

############################################################
# Problem 1b: Solve the segmentation problem under a unigram model

class SegmentationProblem(util.SearchProblem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def startState(self):
        return self.query

    def isGoal(self, state):
        return len(state) == 0

    def succAndCost(self, state):
        result = [] # action, state, cost
        split_prefixes = [(state[:i+1], state[i+1:]) for i in range(len(state))]
        for prefix_word in split_prefixes:
            result.append( (prefix_word[0], prefix_word[1],  self.unigramCost( prefix_word[0]) ) )
        return( result )

def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))

    answer = query
    if( len(ucs.actions) ):
        answer = ' '.join( ucs.actions )

    return answer




############################################################
# Problem 2b: Solve the vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        return ( wordsegUtil.SENTENCE_BEGIN, tuple(self.queryWords) )

    def isGoal(self, state):
        return len(state[1]) == 0

    def succAndCost(self, state):
        result = [] # action, state, cost
        if( len(state[1]) >= 1):
            pfills = self.possibleFills( state[1][0] )
            if(len(pfills)==0): pfills = set( [ state[1][0] ] )
            for wrd in pfills:
                result.append( (wrd, (wrd, tuple(state[1][1:])), self.bigramCost(state[0], wrd)) )
        return( result )


def insertVowels(queryWords, bigramCost, possibleFills):

    if queryWords is None:
        return ''
    if len(queryWords) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(VowelInsertionProblem(queryWords, bigramCost, possibleFills))

    answer = ' '.join( queryWords )
    if ucs.actions is None:
        return answer
    elif( len(ucs.actions) ):
        answer = ' '.join( ucs.actions )
    return answer



############################################################
# Problem 3b: Solve the joint segmentation-and-insertion problem

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        return ( wordsegUtil.SENTENCE_BEGIN, self.query )

    def isGoal(self, state):
        return len(state[1]) == 0

    def succAndCost(self, state):
        result = [] # action, state, cost
        split_prefixes = [(state[1][:i+1], state[1][i+1:]) for i in range(len(state[1]))]
        for prefix_word in split_prefixes:
            if( len(state[1]) >= 1):
                pfills = self.possibleFills( prefix_word[0] )
                for wrd in pfills:
                    result.append( (wrd, (wrd, prefix_word[1]), self.bigramCost(state[0], wrd)) )
        return( result )

def segmentAndInsert(query, bigramCost, possibleFills):
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(JointSegmentationInsertionProblem(query, bigramCost, possibleFills))

    answer = query
    if ucs.actions is None:
        return answer
    elif( len(ucs.actions) ):
        answer = ' '.join( ucs.actions )
    return answer




############################################################

#if __name__ == '__main__':
#    shell.main()
