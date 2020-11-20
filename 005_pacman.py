from util import manhattanDistance
from game import Directions
import random, util

from game import Agent




class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """
  def __init__(self):
    self.lastPositions = []
    self.dc = None


  def getAction(self, gameState):
    """
    getAction chooses among the best options according to the evaluation function.

    getAction takes a GameState and returns some Directions.X for some X in the set {North, South, West, East, Stop}
    ------------------------------------------------------------------------------
    Description of GameState and helper functions:

    A GameState specifies the full game state, including the food, capsules,
    agent configurations and score changes. In this function, the |gameState| argument 
    is an object of GameState class. Following are a few of the helper methods that you 
    can use to query a GameState object to gather information about the present state 
    of Pac-Man, the ghosts and the maze.
    
    gameState.getLegalActions(): 
        Returns the legal actions for the agent specified. Returns Pac-Man's legal moves by default.

    gameState.generateSuccessor(agentIndex, action): 
        Returns the successor state after the specified agent takes the action. 
        Pac-Man is always agent 0.

    gameState.getPacmanState():
        Returns an AgentState object for pacman (in game.py)
        state.configuration.pos gives the current position
        state.direction gives the travel vector

    gameState.getGhostStates():
        Returns list of AgentState objects for the ghosts

    gameState.getNumAgents():
        Returns the total number of agents in the game

    gameState.getScore():
        Returns the score corresponding to the current state of the game

    
    The GameState class is defined in pacman.py and you might want to look into that for 
    other helper methods, though you don't need to.
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best




    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (oldFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    oldFood = currentGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]


    return successorGameState.getScore()


def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)













######################################################################################
# Problem 1b: implementing minimax


class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (problem 1)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction. Terminal states can be found by one of the following: 
      pacman won, pacman lost or there are no legal moves. 

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game

      gameState.getScore():
        Returns the score corresponding to the current state of the game
    
      gameState.isWin():
        Returns True if it's a winning state
    
      gameState.isLose():
        Returns True if it's a losing state

      self.depth:
        The depth to which search should continue

    """

    def isEnd(gState):
        return( gState.isWin() or gState.isLose() )

    def recurse( gState, depth, agent ):
        if isEnd(gState): return (gState.getScore(), Directions.STOP )
        elif depth == 0: return (self.evaluationFunction( gState ), Directions.STOP)
        actions = gState.getLegalActions( agent )
        if agent == 0: actions = [ mv for mv in actions if mv != Directions.STOP ]
        sccStates = [(gState.generateSuccessor( agent, action), action) for action in actions]
        thisAgent = agent
        if thisAgent == gState.getNumAgents()-1: #last ghost
            depth, agent  = depth - 1, self.index
        else:  agent += 1
        valueSA = [(recurse( state, depth, agent )[0] , action) for state, action in sccStates ]
        if thisAgent == 0: #pacman
            return max( valueSA )
        elif thisAgent <= gState.getNumAgents()-1 : #ghosts
            return min( valueSA )

    return recurse( gameState, self.depth, self.index )[1]









######################################################################################
# Problem 2a: implementing alpha-beta

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (problem 2)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """

    def isEnd(gState):
        return( gState.isWin() or gState.isLose() )

    def recurse( gState, depth, agent, alpha, beta ):
        if isEnd(gState): return (gState.getScore(), Directions.STOP )
        elif depth == 0: return (self.evaluationFunction( gState ), Directions.STOP)
        actions = gState.getLegalActions( agent )
        if agent == 0: actions = [ mv for mv in actions if mv != Directions.STOP ]
        sccStates = [(gState.generateSuccessor( agent, action), action) for action in actions]
        thisAgent = agent
        if thisAgent == gState.getNumAgents()-1: #last ghost
            depth, agent  = depth - 1, self.index
        else:  agent += 1

        valueSA  = []
        for state, action in sccStates:
            value = recurse( state, depth, agent, alpha, beta )[0]
            valueSA.append( (value, action) )

            if(thisAgent == 0 and value > alpha ):
                if( value > beta ): break  #pruning
                alpha = value

            if( thisAgent != 0 and value < beta ):
                if( value < alpha ): break   #pruning
                beta = value

        if thisAgent == 0: #pacman
            return max( valueSA )
        elif thisAgent <= gState.getNumAgents()-1 : #ghosts
            return min( valueSA )

    value, action = recurse( gameState, self.depth, self.index, -float("inf"), float("inf") )
    return action




######################################################################################
# Problem 3b: implementing expectimax

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (problem 3)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """

    def isEnd(gState):
        return( gState.isWin() or gState.isLose() )

    def recurse( gState, depth, agent ):
        if isEnd(gState): return (gState.getScore(), Directions.STOP )
        elif depth == 0: return (self.evaluationFunction( gState ), Directions.STOP)
        actions = gState.getLegalActions( agent )
        if agent == 0: actions = [ mv for mv in actions if mv != Directions.STOP ]
        sccStates = [(gState.generateSuccessor( agent, action), action) for action in actions]
        thisAgent = agent
        if thisAgent == gState.getNumAgents()-1: #last ghost
            depth, agent  = depth - 1, self.index
        else:  agent += 1
        valueSA = [(recurse( state, depth, agent )[0] , action) for state, action in sccStates ]
        if thisAgent == 0: #pacman
            bestScore = max( valueSA )
            bestIndices = [index for index in range(len(valueSA)) if valueSA[index][0] == bestScore[0]]
            chosenIndex = random.choice(bestIndices) # Pick randomly among the best
            return valueSA[ chosenIndex ]
        elif thisAgent <= gState.getNumAgents()-1 : #ghosts
            summ = 0
            for v in valueSA: summ += v[0]
            return ( summ / len(valueSA), Directions.STOP )

    return recurse( gameState, self.depth, self.index )[1]





######################################################################################
# Problem 4a (extra credit): creating a better evaluation function

# Explanations contained in comments

def manhattanDistance(a, b):
    return abs(float(a[0]) - float(b[0])) + abs(float(a[1]) - float(b[1]) )

lastCapsuleCount = 0

def betterEvaluationFunction(gs):

    #####
    #
    # TODO: GET RID OF GLOBAL VARIABLE AND ALSO, USE A KDTREE OR A QUADTREE FOR OVERALL SPEED UP.
    #

    global lastCapsuleCount

    score = gs.getScore()
    pacmanState = gs.getPacmanState()
    pacmanLocation = gs.getPacmanPosition()
    ghostPositions = gs.getGhostPositions()
    capsuleLocations = gs.getCapsules()

    ######
    #
    # Go straight towards capsules b/c eating them lets you hunt ghosts & get more points!
    #
    if len(capsuleLocations ):
        capAdd = 1.0 / ((min(mazeDistance(pacmanLocation, capsuleLoc, gs) for capsuleLoc in capsuleLocations))+0.01 )
        score += capAdd**2

    ###
    #
    # Simulated some incentives to activate bloodthirsty ghost hunting:
    # since the game didn't a way to internally get or query points for this
    #
    if(lastCapsuleCount > len(capsuleLocations ) ):
        score += 100.0

    ######
    #
    # Super basic ghost hunting:
    #
    ghostStates = gs.getGhostStates()

    #save ghost distances b/c we will use them a couple times and it's expensive:
    ghostGraphDistances = []
    for gloc in ghostPositions:
        ghostGraphDistances.append( mazeDistance(pacmanLocation, (int(gloc[0]),int(gloc[1])), gs) )

    # Hunt them like helpless prey (should still avoid the dangerous ones)
    g=0
    scareTimer = False
    if len(ghostPositions):
        for ghost in ghostStates:
            if( ghost.scaredTimer > 0 ):
                scareTimer = True
                #print "YOU BETTER BE SCARED YOU GHOST FACE CHILLAS!!"
                ghostScoreAdd =  1.0 / (ghostGraphDistances[g] +0.01)
                ghostScoreAdd = ghostScoreAdd * 100.0
                score += ghostScoreAdd
            g += 1

   # Simple enhanced ghost defense (see around corners better)
    totalGhostDistance = 0
    for ghost in ghostGraphDistances:
        totalGhostDistance += float(ghost)
    if( totalGhostDistance < 2.0 and not scareTimer ): return -9999

    ###
    # Food Grid (so delicious)
    # Get ready to eat!
    #
    foodDistances = []
    food = gs.getFood()
    walls = gs.getWalls()
    i,j=0,0

    ####
    #
    # Stay hungry.  Stay foolish.  Definitely foolish...
    #
    # First calculate a heuristic notion of the nearest food pellets
    #
    for columns in food:
        j=0
        for row in columns:
            if( food[i][j] == True ):
                if not walls[i][j]:
                    #
                    # Lots of food and data, use rough heuristics first:
                    #
                    dist = manhattanDistance(pacmanLocation,  (float(i),float(j)) )
                    if(dist > 0 ):  foodDistances.append( (dist,(i, j) )  )
            j += 1
        i += 1

    moreAccurateFoodDs = sorted(foodDistances )

    ################
    #
    # Now use real distance through the maze based on the smallest sorted heuristic values:
    #
    f=0
    for foodD in foodDistances:
        if( f < 4 ):
            #if(len(foodDistances) == 1): print "Coordinates= pacman: ", pacmanLocation, "   food: ", foodD[1]
            moreAccurateFoodDs[f] = ( mazeDistance( pacmanLocation,  foodD[1], gs ), foodD[1] )
        f += 1

    if len(moreAccurateFoodDs):
        capAdd = 1.0 / ((min(moreAccurateFoodDs)[0] )+0.01 )
        score += capAdd

    lastCapsuleCount = len(capsuleLocations)

    #print "Pacman coordinates: ", pacmanLocation

    return score








  #
  #
  # def getLegalPacmanActions( self ):
  #   return self.getLegalActions( 0 )
  #
  # def generatePacmanSuccessor( self, action ):
  #   """
  #   Generates the successor state after the specified pacman move
  #   """
  #   return self.generateSuccessor( 0, action )
  #
  # def getPacmanState( self ):
  #   """
  #   Returns an AgentState object for pacman (in game.py)
  #
  #   state.configuration.pos gives the current position
  #   state.direction gives the travel vector
  #   """
  #   return self.data.agentStates[0].copy()
  #
  # def getPacmanPosition( self ):
  #   return self.data.agentStates[0].getPosition()
  #
  # def getGhostStates( self ):
  #   return self.data.agentStates[1:]
  #
  # def getGhostState( self, agentIndex ):
  #   if agentIndex == 0 or agentIndex >= self.getNumAgents():
  #     raise Exception("Invalid index passed to getGhostState")
  #   return self.data.agentStates[agentIndex]
  #
  # def getGhostPosition( self, agentIndex ):
  #   if agentIndex == 0:
  #     raise Exception("Pacman's index passed to getGhostPosition")
  #   return self.data.agentStates[agentIndex].getPosition()
  #
  # def getGhostPositions(self):
  #   return [s.getPosition() for s in self.getGhostStates()]
  #
  # def getNumAgents( self ):
  #   return len( self.data.agentStates )
  #
  # def getScore( self ):
  #   return self.data.score
  #
  # def getCapsules(self):
  #   """
  #   Returns a list of positions (x,y) of the remaining capsules.
  #   """
  #   return self.data.capsules
  #
  # def getNumFood( self ):
  #   return self.data.food.count()
  #
  # def getFood(self):
  #   """
  #   Returns a Grid of boolean food indicator variables.
  #
  #   Grids can be accessed via list notation, so to check
  #   if there is food at (x,y), just call
  #
  #   currentFood = state.getFood()
  #   if currentFood[x][y] == True: ...
  #   """
  #   return self.data.food
  #
  # def getWalls(self):
  #   """
  #   Returns a Grid of boolean wall indicator variables.
  #
  #   Grids can be accessed via list notation, so to check
  #   if there is food at (x,y), just call
  #
  #   walls = state.getWalls()
  #   if walls[x][y] == True: ...
  #   """
  #   return self.data.layout.walls
  #
  # def hasFood(self, x, y):
  #   return self.data.food[x][y]
  #
  # def hasWall(self, x, y):
  #   return self.data.layout.walls[x][y]
  #
  # def isLose( self ):
  #
  # def isWin( self ):
  #










###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
# library code for search below
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################








from util import manhattanDistance
from game import Directions
from game import Actions
import random, util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()

class PositionSearchProblem(SearchProblem):
    """
    A search problem defines the state space, start state, goal test,
    successor function and cost function.  This search problem can be
    used to find paths to a particular point on the pacman board.
    The state space consists of (x,y) positions in a pacman game.
    Note: this search problem is fully specified; you should NOT change it.
    """

    def __init__(self, gameState, costFn = lambda x: 1, goal=(1,1), start=None, warn=True, visualize=True):
        """
        Stores the start and goal.
        gameState: A GameState object (pacman.py)
        costFn: A function from a search state (tuple) to a non-negative number
        goal: A position in the gameState
        """
        self.walls = gameState.getWalls()
        self.startState = gameState.getPacmanPosition()
        if start != None: self.startState = start
        self.goal = goal
        self.costFn = costFn
        self.visualize = visualize
        if warn and (gameState.getNumFood() != 1 or not gameState.hasFood(*goal)):
            print 'Warning: this does not look like a regular search maze'

        # For display purposes
        self._visited, self._visitedlist, self._expanded = {}, [], 0 # DO NOT CHANGE

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        isGoal = state == self.goal

        # For display purposes only
        if isGoal and self.visualize:
            self._visitedlist.append(state)
            import __main__
            if '_display' in dir(__main__):
                if 'drawExpandedCells' in dir(__main__._display): #@UndefinedVariable
                    __main__._display.drawExpandedCells(self._visitedlist) #@UndefinedVariable

        return isGoal

    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.
         As noted in search.py:
             For a given state, this should return a list of triples,
         (successor, action, stepCost), where 'successor' is a
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental
         cost of expanding to that successor
        """

        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x,y = state
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextState = (nextx, nexty)
                cost = self.costFn(nextState)
                successors.append( ( nextState, action, cost) )

        # Bookkeeping for display purposes
        self._expanded += 1 # DO NOT CHANGE
        if state not in self._visited:
            self._visited[state] = True
            self._visitedlist.append(state)

        return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999
        """
        if actions == None: return 999999
        x,y= self.getStartState()
        cost = 0
        for action in actions:
            # Check figure out the next state and see whether its' legal
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
            cost += self.costFn((x,y))
        return cost

class Node():
  """
  A container storing the current state of a node, the list
  of  directions that need to be followed from the start state to
  get to the current state and the specific problem in which the
  node will be used.
  """
  def __init__(self, state, path, cost=0, heuristic=0, problem=None):
    self.state = state
    self.path = path
    self.cost = cost
    self.heuristic = heuristic
    self.problem = problem

  def __str__(self):
    string = "Current State: "
    string += __str__(self.state)
    string += "\n"
    string == "Path: " + self.path + "\n"
    return string

  def getSuccessors(self, heuristicFunction=None):
    children = []
    for successor in self.problem.getSuccessors(self.state):
      state = successor[0]
      path = list(self.path)
      path.append(successor[1])
      cost = self.cost + successor[2]
      if heuristicFunction:
        heuristic = heuristicFunction(state, self.problem)
      else:
        heuristic = 0
      node = Node(state, path, cost, heuristic, self.problem)
      children.append(node)
    return children

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """

    closed = set()
    fringe = util.Queue()

    startNode = Node(problem.getStartState(), [], 0, 0, problem)
    fringe.push(startNode)

    while True:
      if fringe.isEmpty():
        return False
      node = fringe.pop()
      if problem.isGoalState(node.state):
        return node.path
      if node.state not in closed:
        closed.add(node.state)
        for childNode in node.getSuccessors():
          fringe.push(childNode)

def mazeDistance(point1, point2, gameState):
    """
    Returns the maze distance between any two points, using the search functions
    you have already built.  The gameState can be any game state -- Pacman's position
    in that state is ignored.
    Example usage: mazeDistance( (2,4), (5,6), gameState)
    This might be a useful helper function for your ApproximateSearchAgent.
    """
    x1, y1 = point1
    x2, y2 = point2
    walls = gameState.getWalls()
    assert not walls[x1][y1], 'point1 is a wall: ' + point1
    assert not walls[x2][y2], 'point2 is a wall: ' + str(point2)
    prob = PositionSearchProblem(gameState, start=point1, goal=point2, warn=False, visualize=False)
    return len(breadthFirstSearch(prob))











# Abbreviation
better = betterEvaluationFunction































