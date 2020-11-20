
def read(fn):
    # also look at readline() and readlines() functions
    return open(fn,'r').read()

def read_filter_split(fn):
    s = open(fn,'r').read()
    return [w for w in s.split() if w.isalnum()]

x = {'and':'of', 'square':'root', 'center':'point', 'microscope':'image'}

