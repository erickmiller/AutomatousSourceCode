from subtract_square_state import SubtractSquareState

class GameStateNode:
    '''
    A tree of possible states for a two-player, sequential move, zero-sum,
    perfect-information game.

    value: GameState -- the game state at the root of this tree
    children: list -- all possible game states that can be reached from this
 	game state via one legal move in the game.  children is None until grow
	is called.
    '''

    def __init__(self, game_state):
        ''' (GameStateNode, GameState) -> NoneType

        Initialize a new game state tree consisting of a single root node 
	that contains game_state.
        '''
        self.value = game_state
        self.children = []

    def __eq__(self, other):
        ''' (GameStateNode, object) -> bool

        Return whether this GameStateNode is equivalent to other, i.e., they
        contain equivalent GameStates, and equivalent children.  The order of
        their children does not matter.

        >>> s1 = SubtractSquareState('p1', current_total = 6)
        >>> s2 = SubtractSquareState('p2', current_total = 5)
        >>> s3 = SubtractSquareState('p1', current_total = 2)
        >>> leaf1 = GameStateNode(s1)
        >>> leaf2 = GameStateNode(s2)
        >>> leaf3 = GameStateNode(s3)
        >>> leaf1.__eq__(leaf2)
        False
        >>> root1 = GameStateNode(s1)
        >>> root1.children = [s2, s3]
        >>> root2 = GameStateNode(s1)
        >>> root1.__eq__(root2)
        False
        >>> root2.children = [s2, s3]
        >>> root1.__eq__(root2)
        True
        '''
        # Checking that the children lists have the same contents requires
        # checking that every element of one list is in the other, and vice
        # versa. Since checking "in" causes calls to the __eq__ method, we
        # end up recursing.
        return (type(self) == type(other) and
                self.value == other.value and        
                same_contents(self.children, other.children))


    def __str__(self):
        ''' (GameStateNode) -> str

        Return a convenient string representation of GameStateNode(self).

        >>> s = SubtractSquareState('p1', current_total = 17)
        >>> node = GameStateNode(s)
        >>> print(node)
        Current total: 17; next player: p1
        '''
        return self.value.__str__()


    def grow(self):
        ''' (GameStateNode) -> NoneType

        Grow the tree of all possible game state nodes that can be reached
	starting from this one.

        Assume that the game is finite (and so the tree will be finite).
        
        >>> a0 = SubtractSquareState('p1', current_total = 0)
        >>> b1 = SubtractSquareState('p2', current_total = 1)
        >>> a2 = SubtractSquareState('p1', current_total = 2)
        >>> b3 = SubtractSquareState('p2', current_total = 3)
        >>> a4 = SubtractSquareState('p1', current_total = 4)
        >>> b0 = SubtractSquareState('p2', current_total = 0)
        >>> a0_node = GameStateNode(a0)
        >>> b1_node = GameStateNode(b1)
        >>> b1_node.children = [a0_node]
        >>> a2_node = GameStateNode(a2)
        >>> a2_node.children = [b1_node]
        >>> b3_node = GameStateNode(b3)
        >>> b3_node.children = [a2_node]
        >>> b0_node = GameStateNode(b0)
        >>> a4_node = GameStateNode(a4)
        >>> a4_node.children = [b0_node, b3_node]
        >>> root = GameStateNode(SubtractSquareState('p1', current_total = 4))
        >>> root.grow()
        >>> root.__eq__(a4_node)
        True
        '''
        self.children = []
        moves = self.value.possible_next_moves()
        for move in moves:
            state = self.value.apply_move(move)
            node = GameStateNode(state)
            node.grow()
            self.children.append(node)


def same_contents(L1, L2):
    ''' (list, list) -> bool
    
    Return True iff L1 and L2 have the same contents, although not necessarily
    in the same order.
    
    >>> same_contents([1, 4, 5, 2], [5, 2, 4, 1])
    True
    >>> same_contents([1, 2], [2, 1, 1])
    False
    '''
    return (len(L1) == len(L2) and 
            all([x in L2 for x in L1]) and 
            all([x in L1 for x in L2]))


def _nodes(root):
    ''' (GameStateNode) -> list
    
    Return the list of nodes in the tree rooted at root.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> len(_nodes(root))
    13
    '''
    nodes = [root]
    for node in root.children:
        nodes += _nodes(node)
    return nodes


def node_count(root):
    ''' (GameStateNode) -> int
    
    Return the number of nodes in the tree rooted at root.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> node_count(root)
    13
    '''
    return len(_nodes(root))


def _leafs(root):
    '''(GameStateNode) -> list
    
    Return the list of leaves in the tree rooted at root.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> len(_leafs(root))
    4
    '''
    leafs = []
    if root.value.over:
        leafs.append(root)
    for node in root.children:
        leafs += _leafs(node)
    return leafs


def leaf_count(root):
    '''(GameStateNode) -> int
    
    Return the number of leaves in the tree rooted at root.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> leaf_count(root)
    4
    '''
    return len(_leafs(root))


def _distinct_nodes(root):
    '''(GameStateNode) -> set
    
    Return the set of nodes representing distinct game states in the
    tree rooted at root.  Two game states are distinct if they are not __eq__.

    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> len(_distinct_nodes(root))
    10
    '''
    nodes = set()
    nodes.add(str(root))
    for node in root.children:
        nodes |= _distinct_nodes(node)
    return nodes


def distinct_node_count(root):
    '''(GameStateNode) -> int
    
    Return the number of nodes representing distinct game states in the
    tree rooted at root.  Two game states are distinct if they are not __eq__.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> distinct_node_count(root)
    10
    '''
    return len(_distinct_nodes(root))


def _distinct_leafs(root):
    '''(GameStateNode) -> set
    
    Return the set of leaves representing distinct game states in the
    tree rooted at root.

    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> len(_distinct_leafs(root))
    2
    '''
    leafs = set()
    if root.value.over:
        leafs.add(str(root))
    for node in root.children:
        leafs |= _distinct_leafs(node)
    return leafs
                      

def distinct_leaf_count(root):
    '''
    (GameStateNode) -> int
    
    Return the number of leaves representing distinct game states in the
    tree rooted at root.
       
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> distinct_leaf_count(root)
    2
    '''
    return len(_distinct_leafs(root))


def branching_stats(root):
    ''' (GameStateNode) -> {int: int}
    
    Return a dict that represents the distribution of branching factors in
    the tree rooted at root. Each key is a branching factor >= 0, and its
    value is the number of nodes with that branching factor.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> branching_stats(root) == {0: 4, 1: 6, 2: 3}
    True
    '''
    result = {}
    nodes = _nodes(root)
    for i in range(len(nodes)):
        count = 0
        for node in nodes:
            if len(node.children) == i:
                count += 1
        if count > 0:
            result[i] = count
    return result

            
def outcome_counts(root):
    ''' (GameStateNode) -> [int, int, int]
    
    Return a list containing the number of leaf nodes containing a state in
    which player 'p1' is the winner, the number in which player 'p2' is, and
    the number in which the outcome of the game is a tie.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> outcome_counts(root)
    [3, 1, 0]
    '''
    leafs = _leafs(root)
    p1 = p2 = tie = 0
    for leaf in leafs:
        if leaf.value.winner("p1"):
            p1 += 1
        elif leaf.value.winner("p2"):
            p2 += 1
        else:
            tie += 1
    return [p1, p2, tie]


def _games(root, games=[], t=[]):
    '''(GameStateNode, games, t) -> list of list

    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> len(_games(root))
    4
    '''
    t = t + [root]
    if root.value.over:
        games = games + [t]
    for node in root.children:
        games = _games(node, games, t)
    return games


def game_lengths(root):
    ''' (GameStateNode) -> {int: int}
    
    Return a dict that represents the distribution of game lengths in the
    tree rooted at root. Each key is a length of game >= 1, and its value is
    the number of games that are that long. The length of a game is the
    number of moves in the game.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> game_lengths(root) == {6: 1, 3: 3}
    True
    '''
    result = {}
    games = _games(root)
    for game in games:
        lenght = len(game) - 1
        result[lenght] = result.get(lenght, 0) + 1
    return result


def game_descriptions(root):
    ''' (GameStateNode) -> list of str
    
    Return a list containing a str describing each complete game that is
    possible from the game stored at root.
    
    Assume root is the root of a game state tree specifically for the game
    Subtract Square.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> game_descriptions(root)
    ['p1:6 -> p2:2 -> p1:1 -> p2:0 = p1 wins!', 'p1:6 -> p2:5 -> p1:1 -> p2:0 = p1 wins!', 'p1:6 -> p2:5 -> p1:4 -> p2:0 = p1 wins!', 'p1:6 -> p2:5 -> p1:4 -> p2:3 -> p1:2 -> p2:1 -> p1:0 = p2 wins!']
    '''
    descriptions = []
    games = _games(root)
    for game in games:
        abbreviateds = [abbreviated(node.value) for node in game]
        description = " -> ".join(abbreviateds)
        if game[-1].value.winner("p1"):
            description += " = p1 wins!"
        elif game[-1].value.winner("p2"):
            description += " = p2 wins!"
        else:
            description += " = tie!"
        descriptions.append(description)
    return descriptions   

            
def abbreviated(s):
    '''(GameState) -> str
    
    Return an abbreviated str representation of SubtractSquareState s.
    '''
    
    return "{}:{}".format(s.next_player, s.current_total)

if __name__ == '__main__':
    import doctest
    doctest.testmod()


