import re
file = open('words.txt','r')
pattern = re.compile('[\\w]+') #matches alpha numeric in double quotes
word_list = re.findall(pattern, file.read())

sorted_word_list = sorted([sorted(word) for word in word_list])

#print [sorted_word_list[x] for x in range(0,20)]

valid_sorts = []

def equal_lists(list_a, list_b):
    if(len(list_a) != len(list_b)):
        return False
    for i in range(0, len(list_a)):
        if(list_a[i] != list_b[i]):
            return False
    return True
current_match = []
previous_word = []    
for i in range(0,len(sorted_word_list)):
    word = sorted_word_list[i]

    if not equal_lists(word, current_match):
        if equal_lists(word, previous_word):
            valid_sorts = valid_sorts + [word]
            current_match = word
    previous_word = [x for x in word]
    
print len(valid_sorts)
#print valid_sorts

anagram_groups = [[] for x in valid_sorts]
for word in word_list:
    sorted_word = sorted(word)
    for i in range(0,len(valid_sorts)):
        if equal_lists(sorted_word, valid_sorts[i]):
            anagram_groups[i] = anagram_groups[i] + [word]
            
for x in anagram_groups:
    if len(x) > 2:
        print x
        #only one anagram set has more than 2 words in it
        
def is_square(n):
    root = float(n) ** .5
    root = int(root+.5)
    if root*root == n:
        return root
    else:
        return False

def to_num(list):
    sum = 0
    for i in list:
        sum = sum*10
        sum +=i
    return sum        
        
def to_list(num):
    result = []
    val = num
    while(val >0):
        result = [val%10] + result
        val = val/10
    return result
    
best_square = 0
        
for group in anagram_groups:
    for a in range(0, len(group) - 1):
        for b in range(a+1,len(group)):
            word_a = group[a]
            word_b = group[b]
            min_x = int((10**(len(word_a)-1)) ** .5)
            man_x = int((10**len(word_a)) ** .5)
            for x in range(min_x,man_x):
                vals_used = [False]*10
                square = x*x
                valid = True
                square_list = to_list(square)
                if(len(square_list) == len(word_a)):
                    sub_a = [x for x in word_a]
                    sub_b = [x for x in word_b]
                    for i in range(0,len(square_list)):
                        if not valid:
                            break
                        letter_sub = sub_a[i]
                        if letter_sub > 10: #will always be true for characters never digits
                            sub_val = square_list[i]
                            if(vals_used[sub_val]):
                                valid = False
                                break
                            vals_used[sub_val] = True    
                            for j in range(0,len(square_list)):
                                if(sub_a[j] == letter_sub):
                                    #trying to replace something with wrong digit
                                    if(square_list[j] != sub_val): 
                                        valid = False
                                        break
                                    sub_a[j] = sub_val #so i don't repeat subbing digits
                                if(sub_b[j] == letter_sub):
                                    if(j == 0 and sub_val == 0):
                                        valid = False
                                        break
                                    sub_b[j] = sub_val
                    if(valid):
                        square_a = to_num(sub_a)
                        if(square_a != square):
                            print "assertion failed", square_a, "not", square
                        square_b = to_num(sub_b)
                        if is_square(square_b):
                            #print "found match"
                            found_square = max(square_a, square_b)
                            if(found_square > best_square):
                                best_square = found_square
                                print "new best", square_a, square_b, "with group ", group
                                
        
print "largest square is", best_square