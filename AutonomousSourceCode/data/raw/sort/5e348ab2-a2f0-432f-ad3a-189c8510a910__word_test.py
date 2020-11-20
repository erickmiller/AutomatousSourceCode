def word_dic(filename):
    dic = {}
    fin = open(filename)
    for line in fin:
        s = line.strip()
        t = sorted_word(s)
        if t not in dic:
            dic[t] = [s]
        else:
            dic[t] += [s]
    return dic

def sorted_word(s):
    li = list(s)
    li.sort()
    s = "".join(li)
    return s
