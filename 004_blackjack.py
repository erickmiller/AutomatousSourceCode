import collections, util, math, random


############################################################
class ValueIteration(util.MDPAlgorithm):
    '''
    Solve the MDP using value iteration.  Your solve() method must set
    - self.V to the dictionary mapping states to optimal values
    - self.pi to the dictionary mapping states to an optimal action
    Note: epsilon is the error tolerance: you should stop value iteration when
    all of the values change by less than epsilon.
    The ValueIteration class is a subclass of util.MDPAlgorithm (see util.py).
    '''
    def solve(self, mdp, epsilon=0.001):
        mdp.computeStates()
        def computeQ(mdp, V, state, action):
            # Return Q(state, action) based on V(state).
            return sum(prob * (reward + mdp.discount() * V[newState]) \
                            for newState, prob, reward in mdp.succAndProbReward(state, action))

        def computeOptimalPolicy(mdp, V):
            # Return the optimal policy given the values V.
            pi = {}
            for state in mdp.states:
                pi[state] = max((computeQ(mdp, V, state, action), action) for action in mdp.actions(state))[1]
            return pi

        V = collections.Counter()  # state -> value of state
        numIters = 0
        while True:
            newV = {}
            for state in mdp.states:
                newV[state] = max(computeQ(mdp, V, state, action) for action in mdp.actions(state))
            numIters += 1
            if max(abs(V[state] - newV[state]) for state in mdp.states) < epsilon:
                V = newV
                break
            V = newV

        # Compute the optimal policy now
        pi = computeOptimalPolicy(mdp, V)
        print "ValueIteration: %d iterations" % numIters
        self.pi = pi
        self.V = V


############################################################
# Problem 2a

# If you decide 2a is true, prove it in writeup.pdf and put "return None" for
# the code blocks below.  If you decide that 2a is false, construct a counterexample.
class CounterexampleMDP(util.MDP):
    def startState(self):
        return 0

    # Return set of actions possible from |state|.
    def actions(self, state):
        if state == 0:
            return ['action']
        else:
            return ['terminate']

    #def isEnd(self, state):
    #    return (state == 1 or state == -1)

    # Return a list of (newState, prob, reward) tuples corresponding to edges
    # coming out of |state|.
    def succAndProbReward(self, state, action):
        results = [] # state, probability, reward

        if not (state == 1 or state == -1):
            results.append( ( -1, .9, 10 ) )
            results.append( ( 1, .1, 1000 ) )
            # test:
            #results.append( ( -1, .7, 10 ) )
            #results.append( ( 1, .3, 1000 ) )

        return results

    def discount(self):
        return 1




############################################################
# Problem 3a

class BlackjackMDP(util.MDP):
    def __init__(self, cardValues, multiplicity, threshold, peekCost):
        """
        cardValues: array of card values for each card type
        multiplicity: number of each card type
        threshold: maximum total before going bust
        peekCost: how much it costs to peek at the next card
        """
        self.cardValues = cardValues
        self.multiplicity = multiplicity
        self.threshold = threshold
        self.peekCost = peekCost

    # Return the start state.
    # Look at this function to learn about the state representation.
    # The first element of the tuple is the sum of the cards in the player's
    # hand.
    # The second element is the index (not the value) of the next card,
    # if the player peeked in the
    # last action.  If they didn't peek, this will be None.
    # The final element is the current deck.
    def startState(self):
        # total, next card (if any), multiplicity for each card
        return (0, None, (self.multiplicity,) * len(self.cardValues))

    # Return set of actions possible from |state|.
    # You do not need to modify this function.
    # All logic for dealing with end states should be done in succAndProbReward
    def actions(self, state):
        return ['Take', 'Peek', 'Quit']

    # Return a list of (newState, prob, reward) tuples corresponding to edges
    # coming out of |state|.  Indicate a terminal state (after quitting or
    # busting) by setting the deck to None. 
    # When the probability is 0 for a particular transition, don't include that 
    # in the list returned by succAndProbReward.
    def succAndProbReward(self, state, action):
        results = [] # successor-state, probability, reward
        cardCounts = state[2]
        if( cardCounts == None ): #no more cards, game over state
            return []

        totalCardsLeft = float(sum( cardCounts ))
        didPeek = (state[1] != None)

        if action is 'Take':
            if( didPeek ):  #peeked on last round...
                newCardCounts = list(cardCounts)
                newCardCounts[ state[1] ] = newCardCounts[ state[1] ] - 1
                if( newCardCounts[ state[1] ] < 0 ): newCardCounts[ state[1] ] = 0.0
                newHoldingValue = state[0] + self.cardValues[ state[1] ]
                cardsLeftNow = float(sum( newCardCounts ))
                busted = (newHoldingValue > self.threshold)
                if( cardsLeftNow == 0.0 and not busted): #no more cards left!
                    return [ ( (newHoldingValue, None, None ), 1.0, newHoldingValue ) ]
                elif( cardsLeftNow == 0.0 and busted): #no more cards but busted ...what a silly silly robot.
                    #print "BUSTED AT LAST CARD AFTER PEEKING!"
                    return [ ( ( newHoldingValue, None, None ), 1.0, 0.0 ) ]
                elif not busted and cardsLeftNow > 0: #not busted, and still more cards
                    return [ ( ( newHoldingValue, None, tuple(newCardCounts) ), 1.0, 0.0) ]
                elif busted and cardsLeftNow > 0: #bust after peeking? really not a very smart robot.
                    #print "BUSTED AFTER PEEKING!"
                    return [ ( ( newHoldingValue, None, None ), 1.0, 0.0 ) ]
            else: #didn't peek last round...
                for i, cardValue in enumerate(self.cardValues):
                    if( cardCounts[i] > 0 ):
                        newCardCounts = list(cardCounts)
                        newCardCounts[ i ] = newCardCounts[ i ] - 1
                        newHoldingValue = state[0] + cardValue
                        cardsLeftNow = float(sum( newCardCounts ))
                        busted = (newHoldingValue > self.threshold)
                        if busted: #bust
                            results.append( ( ( newHoldingValue, None, None ), cardCounts[i]/totalCardsLeft, 0.0 ) )
                        elif( cardsLeftNow <= 0.0 ): #no more cards left!
                            results.append( ( (newHoldingValue, None, None ), 1.0, newHoldingValue ) )
                        elif not busted and cardsLeftNow > 0: #not busted, still more cards:
                            results.append( ((newHoldingValue, None, tuple(newCardCounts)), cardCounts[i]/totalCardsLeft, 0.0 ) )

        if action is 'Peek':
            if( didPeek ): #peeked last time, trying to peek twice? bad robot.
                return []
            else:
                for i, cardValue in enumerate(self.cardValues):
                    if( cardCounts[i] > 0 ):
                        busted = (state[0] > self.threshold)
                        if not busted: #not busted
                            results.append( ((state[0], i, cardCounts), cardCounts[i]/totalCardsLeft, -self.peekCost ) )
                        else: #busted
                            results.append( ( (state[0], None, None ), cardCounts[i]/totalCardsLeft, -self.peekCost ) )

        if action is 'Quit':
            results = [ ( (state[0], None, None ), 1.0, state[0] ) ]

        return results
        # END_YOUR_CODE

    def discount(self):
        return 1







############################################################
# Problem 3b

def peekingMDP():
    """
    Return an instance of BlackjackMDP where peeking is the optimal action at
    least 10% of the time.
    """
    return BlackjackMDP([2,3,19], 7, 20, 1)




############################################################
# Problem 4a: Q learning

# Performs Q-learning.  Read util.RLAlgorithm for more information.
# actions: a function that takes a state and returns a list of actions.
# discount: a number between 0 and 1, which determines the discount factor
# featureExtractor: a function that takes a state and action and returns
# a list of (feature name, feature value) pairs.
# explorationProb: the epsilon value indicating how frequently the policy
# returns a random action
class QLearningAlgorithm(util.RLAlgorithm):
    def __init__(self, actions, discount, featureExtractor, explorationProb=0.2):
        self.actions = actions
        self.discount = discount
        self.featureExtractor = featureExtractor
        self.explorationProb = explorationProb
        self.weights = collections.Counter()
        self.numIters = 0
        self.lastETA = 0

    # Return the Q function associated with the weights and features
    def getQ(self, state, action):
        score = 0.0
        for f, v in self.featureExtractor(state, action):
            score += self.weights[f] * v
        return score

    # This algorithm will produce an action given a state.
    # Here we use the epsilon-greedy algorithm: with probability
    # |explorationProb|, take a random action.
    def getAction(self, state):
        self.numIters += 1
        if random.random() < self.explorationProb:
            return random.choice(self.actions(state))
        else:
            return max((self.getQ(state, action), action) for action in self.actions(state))[1]

    # Call this function to get the step size to update the weights.
    def getStepSize(self):
        return 1.0 / math.sqrt(self.numIters)

    def multF(self, value, phi):
        score = 0.0
        for f, v in phi:
            score += value * v
        return score

    # We will call this function with (s, a, r, s'), which you should use to update |weights|.
    # Note that if s is a terminal state, then s' will be None.  Remember to check for this.
    # You should update the weights using self.getStepSize(); use
    # self.getQ() to compute the current estimate of the parameters.
    #
    def incorporateFeedback(self, state, action, reward, newState):
        eta = self.getStepSize()
        dsc = self.discount
        V_opt = 0.0
        if( newState != None):
            V_opt = max(self.getQ(newState, actn) for actn in self.actions(newState))

        predict = self.getQ(state, action )
        target  = reward + dsc * V_opt
        features = self.featureExtractor(state, action)

        for phi in features:
            self.weights[phi[0]] += -eta*(predict-target) * phi[1]

        # for f, v in features:
        #     #self.weights[f] = (1.0-eta) * Q_opt + eta * (reward + dsc * V_opt)
        #     self.weights[f] = self.weights[f] - eta *( predict - target ) * v



# Return a singleton list containing indicator feature for the (state, action)
# pair.  Provides no generalization.
def identityFeatureExtractor(state, action):
    featureKey = (state, action)
    featureValue = 1
    return [(featureKey, featureValue)]





# ############################################################
# # Problem 4b: convergence of Q-learning
# #
# # "Small" test case ;)
#
# smallMDP = BlackjackMDP(cardValues=[1, 5], multiplicity=2, threshold=10, peekCost=1)
#
# mdp = smallMDP
#
# print "\n\n\n######################################"
# print "######## s m a l l * m d p ###########"
# print "######################################\n"
#
# rl = QLearningAlgorithm(mdp.actions, mdp.discount(), identityFeatureExtractor, .2 )
#
# # simulate(mdp, rl, numTrials=10, maxIterations=1000, verbose=False, sort=False):
#
# trials = util.simulate(mdp, rl, 30000, 1000, False, True )
#
# rl.explorationProb = 0
#
# print "Average rewards of Simulate: "
# print sum(trials) / float(len(trials))
#
# mdp = BlackjackMDP(cardValues=[1, 5], multiplicity=2, threshold=10, peekCost=1)
# vi = ValueIteration()
# vi.solve(mdp)
#
# print "Average rewards of Value Iteration: "
# print sum(vi.V.values() ) / float(len(vi.V.values()))
# #
# # if( list(mdp.states) ==  vi.pi.keys() ):
# #     print "mdp states and value iteration states ARE THE SAME!\n"
# #
# # if( vi.V.keys() == vi.pi.keys() ):
# #     print "V.keys and vi.pi.keys ARE THE SAME!\n"
# #
# #print "vi.V.keys() == ", vi.V.keys()
#
# print "Differences between Simulate (and) Value Iteration: "
# count = 0
# for state, action in vi.pi.iteritems():
#     rlaction = rl.getAction( state )
#     if( action != rlaction):
#         count += 1
#         #print "\n"
#         print "**Value Iteration Policy: \t"+action +":  ",  state
#         print "**Simulate Policy:  \t\t" +rlaction+":  " ,  state
#         #print "\n"
#     #else:
#     #    print "Same Value Iteration Result: \t"+action +":  ",  state
#     #    print "Same Simulate Result:  \t\t" +rlaction+":  " ,  state
#
# print "\nsmall mdp: TOTAL NUM DIFFERENCES BTWN SIM AND VI: " + str( count )
# print "percent error: ", float(count) / float(len(vi.V.keys()))
#
# #print sum( vi.pi.values() ) / float(len( vi.pi.values() ))
#
#
# # Large test case
# largeMDP = BlackjackMDP(cardValues=[1, 3, 5, 8, 10], multiplicity=3, threshold=40, peekCost=1)
#
# mdp = largeMDP
#
# print "\n######################################"
# print "######## L A R G E * M D P ###########"
# print "######################################\n"
#
# rl = QLearningAlgorithm(mdp.actions, mdp.discount(), identityFeatureExtractor, .2 )
#
# # simulate(mdp, rl, numTrials=10, maxIterations=1000, verbose=False, sort=False):
#
# trials = util.simulate(mdp, rl, 30000, 1000, False, True )
#
#
# rl.explorationProb = 0
#
# print "Average rewards of Simulate: "
# print sum(trials) / float(len(trials))
#
# mdp = BlackjackMDP(cardValues=[1, 3, 5, 8, 10], multiplicity=3, threshold=40, peekCost=1)
# vi = ValueIteration()
# vi.solve(mdp)
#
# print "Average rewards of Value Iteration: "
# print sum(vi.V.values() ) / float(len(vi.V.values()))
# #
# # if( list(mdp.states) == list(vi.pi.keys()) ):
# #     print "mdp states and value iteration states ARE THE SAME!\n"
# # else:
# #     print "MDP STATES AND VI STATES NOT SAME? MPD # states = " + str(len(list(mdp.states))) +" Vi num states = " +str(len(vi.pi.keys()))
# #
# # if( vi.V.keys() == vi.pi.keys() ):
# #     print "V.keys and vi.pi.keys ARE THE SAME!\n"
#
# # print "vi.V.keys() == ", vi.V.keys()
#
# print "Differences between Simulate (and) Value Iteration: "
# limitCount = 0
# for state, action in vi.pi.iteritems():
#     rlaction = rl.getAction( state )
#     if( action != rlaction):
#         limitCount += 1
#         if limitCount <= 10:
#             #print "\n"
#             print "**Value Iteration Policy: \t"+action +":  ",  state
#             print "**Simulate Policy:  \t\t" +rlaction+":  " ,  state
#             #print "\n"
#
# print "\nLarge Mdp: TOTAL NUM DIFFERENCES BTWN SIM AND VI: " + str( limitCount )
# print "percent error: ", float(limitCount) / float(len(vi.V.keys()))
#
#     #else:
#     #    print "Same Value Iteration Result: \t"+action +":  ",  state
#     #    print "Same Simulate Result:  \t\t" +rlaction+":  " ,  state
#
#





############################################################
# Problem 4c: features for Q-learning.

# You should return a list of (feature key, feature value) pairs (see
# identityFeatureExtractor()).
# Implement the following features:
# - indicator on the total and the action (1 feature).
# - indicator on the presence/absence of each card and the action (1 feature).
#       Example: if the deck is (3, 4, 0 , 2), then your indicator on the presence
#            of each card is (1,1,0,1)
#       Only add this feature if the deck != None
# - indicator on the number of cards for each card type and the action (len(counts) features).
#   Only add these features if the deck != None
def blackjackFeatureExtractor(state, action):
    total, nextCard, counts = state

    features = []
    featureValue = 1.0
    f = float(total)
    features.append( ( ( 'total_f', f, action), featureValue ) )

    if( counts != None):
        binary = []
        index = 0
        for value in counts:
            binary.append( float(value>0) )
            f = (float(index), float(value))
            features.append( ( ( 'counting_f', f, action), featureValue ) )
            index += 1

        f = tuple(binary)
        features.append( ( ( "binary_f", f, action), featureValue ) )

    return features



#
#
# smallMDP = BlackjackMDP(cardValues=[1, 5], multiplicity=2, threshold=10, peekCost=1)
#
# mdp = smallMDP
#
# print "\n\n\n######################################"
# print "######## s m a l l * m d p ###########"
# print "######################################\n"
#
# rl = QLearningAlgorithm(mdp.actions, mdp.discount(), blackjackFeatureExtractor, .2 )
#
# # simulate(mdp, rl, numTrials=10, maxIterations=1000, verbose=False, sort=False):
#
# trials = util.simulate(mdp, rl, 30000, 1000, False, True )
#
# rl.explorationProb = 0
#
# print "Average rewards of Simulate: "
# print sum(trials) / float(len(trials))
#
# mdp = BlackjackMDP(cardValues=[1, 5], multiplicity=2, threshold=10, peekCost=1)
# vi = ValueIteration()
# vi.solve(mdp)
#
# print "Average rewards of Value Iteration: "
# print sum(vi.V.values() ) / float(len(vi.V.values()))
# #
# # if( list(mdp.states) ==  vi.pi.keys() ):
# #     print "mdp states and value iteration states ARE THE SAME!\n"
# #
# # if( vi.V.keys() == vi.pi.keys() ):
# #     print "V.keys and vi.pi.keys ARE THE SAME!\n"
# #
# #print "vi.V.keys() == ", vi.V.keys()
#
# print "Differences between Simulate (and) Value Iteration: "
# count = 0
# for state, action in vi.pi.iteritems():
#     rlaction = rl.getAction( state )
#     if( action != rlaction):
#         count += 1
#         #print "\n"
#         print "**Value Iteration Policy: \t"+action +":  ",  state
#         print "**Simulate Policy:  \t\t" +rlaction+":  " ,  state
#         #print "\n"
#     #else:
#     #    print "Same Value Iteration Result: \t"+action +":  ",  state
#     #    print "Same Simulate Result:  \t\t" +rlaction+":  " ,  state
#
# print "\nsmall mdp: TOTAL NUM DIFFERENCES BTWN SIM AND VI: " + str( count )
# print "percent error: ", float(count) / float(len(vi.V.keys()))
#
# #print sum( vi.pi.values() ) / float(len( vi.pi.values() ))
#
#
# # Large test case
# largeMDP = BlackjackMDP(cardValues=[1, 3, 5, 8, 10], multiplicity=3, threshold=40, peekCost=1)
#
# mdp = largeMDP
#
# print "\n######################################"
# print "######## L A R G E * M D P ###########"
# print "######################################\n"
#
# rl = QLearningAlgorithm(mdp.actions, mdp.discount(), blackjackFeatureExtractor, .2 )
#
# # simulate(mdp, rl, numTrials=10, maxIterations=1000, verbose=False, sort=False):
#
# trials = util.simulate(mdp, rl, 30000, 1000, False, True )
#
#
# rl.explorationProb = 0
#
# print "Average rewards of Simulate: "
# print sum(trials) / float(len(trials))
#
# mdp = BlackjackMDP(cardValues=[1, 3, 5, 8, 10], multiplicity=3, threshold=40, peekCost=1)
# vi = ValueIteration()
# vi.solve(mdp)
#
# print "Average rewards of Value Iteration: "
# print sum(vi.V.values() ) / float(len(vi.V.values()))
# #
# # if( list(mdp.states) == list(vi.pi.keys()) ):
# #     print "mdp states and value iteration states ARE THE SAME!\n"
# # else:
# #     print "MDP STATES AND VI STATES NOT SAME? MPD # states = " + str(len(list(mdp.states))) +" Vi num states = " +str(len(vi.pi.keys()))
# #
# # if( vi.V.keys() == vi.pi.keys() ):
# #     print "V.keys and vi.pi.keys ARE THE SAME!\n"
#
# # print "vi.V.keys() == ", vi.V.keys()
#
# print "Differences between Simulate (and) Value Iteration: "
# limitCount = 0
# for state, action in vi.pi.iteritems():
#     rlaction = rl.getAction( state )
#     if( action != rlaction):
#         limitCount += 1
#         if limitCount <= 10:
#             #print "\n"
#             print "**Value Iteration Policy: \t"+action +":  ",  state
#             print "**Simulate Policy:  \t\t" +rlaction+":  " ,  state
#             #print "\n"
#
# print "\nLarge Mdp: TOTAL NUM DIFFERENCES BTWN SIM AND VI: " + str( limitCount )
# print "percent error: ", float(limitCount) / float(len(vi.V.keys()))
#
#     #else:
#     #    print "Same Value Iteration Result: \t"+action +":  ",  state
#     #    print "Same Simulate Result:  \t\t" +rlaction+":  " ,  state
#
#
#
#
#















############################################################
# Problem 4d: What happens when the MDP changes underneath you?!
#
# # Original mdp
# originalMDP = BlackjackMDP(cardValues=[1, 5], multiplicity=2, threshold=10, peekCost=1)
#
#
# mdp = originalMDP
# vi = ValueIteration()
# vi.solve(mdp)
#
#
# # New threshold
# newThresholdMDP = BlackjackMDP(cardValues=[1, 5], multiplicity=2, threshold=15, peekCost=1)
#
# mdp = newThresholdMDP
#
# rl = util.FixedRLAlgorithm( vi.pi )
# #rl = QLearningAlgorithm(mdp.actions, mdp.discount(), blackjackFeatureExtractor )
#
#
# trials = util.simulate(mdp, rl, 300, 1000, True, False  )
#







































