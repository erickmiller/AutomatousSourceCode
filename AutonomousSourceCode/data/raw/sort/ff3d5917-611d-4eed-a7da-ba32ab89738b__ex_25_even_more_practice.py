
def break_words(stuff):
    # this function will break up words for us
    w = stuff.split(' ')
    return w

def words_sorted(w):
    # sort words
    s = sorted(w)
    return s

def print_first_word(w):
    #print the first word after popping it off
    p = w.pop(0)
    return p

def print_last_word(w):
    #print the last word after popping it off
    p = w.pop(-1)
    return p

def sort_sentence(s):
    # take in a full sentence and returns the sorted words.
    w = break_words(s)
    return words_sorted(w)

def print_first_and_last(s):
    # prints first and last words of the sentence.
    w = break_words(s)
    return print_first_word(w), print_last_word(w)

def print_f_n_l_sorted(s):
    w = sort_sentence(s)
    return print_first_word(w), print_last_word(w)


ss = "All good things come to those who wait."
w = break_words(ss)

q1 = break_words(ss)
print '1 ', q1
q2 = words_sorted(w)
print '2 ', q2
q3 = print_first_word(w)
print '3 ', q3
q4 = print_last_word(w)
print '4 ', q4
q5 = sort_sentence(ss)
print '5 ', q5
q6 = print_first_and_last(ss)
print '6 ', q6
q7 = print_f_n_l_sorted(ss)
print '7 ', q7


