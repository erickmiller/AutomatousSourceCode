# Create a method that takes 2 words as arguments
# downcase both words
# Sort both words
# Compare both words to see if they match
# Return true or false

# def is_anagram(word_1, word_2):
#     word_1_lower = word_1.lower()
#     word_2_lower = word_2.lower()
#     sorted_word_1 = sorted(word_1_lower)
#     sorted_word_2 = sorted(word_2_lower)
#     return sorted_word_1 ==  sorted_word_2



def canonical(word):
    return sorted(word.lower())

def is_anagram(word_1, word_2):
    return canonical(word_1) == canonical(word_2)

print is_anagram("cat", "dog")
print is_anagram("iceman", "cinema")
