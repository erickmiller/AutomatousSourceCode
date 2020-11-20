from sys import argv
script, first = argv

def make_dict():
    f = open(first)
    filetext = f.read()
    f.close()

    filetext = filetext.split()
    dict_words = {}

    for word in filetext:
        word = word.strip(",.!?-")
        word = word.lower()

        if word not in dict_words:
            dict_words[word] = 1            
        elif word in dict_words:
            dict_words[word] += 1

    return dict_words

def sort_by_frequency(frequency_dict):
    sorted_freq_dict = {}

    for key, value in frequency_dict.iteritems():
        if value not in sorted_freq_dict:
            sorted_freq_dict[value] = [key]
        else:
            sorted_freq_dict[value].append(key)   
    return sorted_freq_dict


def print_sorted_dict(sort_dict):

    num_keys_sort = sorted(sort_dict.keys(), reverse=True)

    for key in num_keys_sort:
        sorted_together = sorted(sort_dict[key])
        for i in sorted_together:
            print str(key) + " " + i

print_sorted_dict(sort_by_frequency(make_dict()))