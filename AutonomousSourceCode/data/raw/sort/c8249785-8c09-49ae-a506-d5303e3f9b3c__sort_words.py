# import re

# def sort_words(s):

#     results = re.findall("[\w;]+", s)
    
#     return "\n".join(map(str, sorted(results)))

# print sort_words(" one, ,two three,4,")


# ############## This works as well

def sort_words(s):
        
    for i in sorted("\n".join(s.split(',')).split()):
        print i

# print count_words(" one, ,two three,4,")

print sort_words(" one, ,two three,4,")