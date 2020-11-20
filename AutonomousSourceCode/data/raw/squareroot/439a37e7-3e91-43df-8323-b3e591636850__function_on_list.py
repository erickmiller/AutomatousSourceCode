# Function handling on list.



lst_a = [1, 2, 3, 4]
lst_b = [5, 6, 7, 8]

func_list = ['square', 'add', 'root']

def list_function(list, function):
    '''(list, function) -> list
    Apply a function to the values of a list and returns a new list.
    >>> list_function([1, 2, 3, 4], add)
    [2, 4, 6, 8]
    >>> list_function([1, 2, 3, 4], square)
    [1, 4, 9, 16]
    list_function([1, 2, 3, 4], root)
    [1.0, 1.4142135623730951, 1.7320508075688772, 2.0]
    '''
    for i in range(len(list)):
        list[i] = function(list[i])
    print list

def square(x):
    '''(number) -> number
    Returns the square of a given number x.
    >>> square(3)
    9
    >>> square(-2)
    4
    >>> square(0)
    0
    '''
    return x ** 2

def add(x):
    '''(number) -> number
    Returns the number added with it self.
    >>> add(3)
    6
    >>> add(-1)
    -2
    '''
    return x + x

def root(x):
    try:
        return x ** 0.5
    except ValueError, e:
        print str(e) + '''.
        List contains negative numbers.'''
    finally:
        print "Remove negative numbers from list and try again."

def choose():
    func_choose = raw_input("Choose function: square = 1, add = 2, root = 3 : ")
    if 1 == int(func_choose):
        return list_function(lst_a, square)
    elif 2 == int(func_choose):
        return list_function(lst_a, add)
    elif 3 == int(func_choose):
        return list_function(lst_a, root)


choose()