import sys

def sort_word(word):
    return "".join(sorted(word))


def is_match(word, sortedWord):
    return sortWord(word.lower()) == sortedWord.lower()


def append_results(words, sorted_input):
    results = []
    for key, value in words.items():
        if value.lower() == sorted_input.lower():
            results.append(key)
    return results


def main(word_input = ""):
    dictionary = open("dict").read().splitlines()
    sorted_input = sort_word(word_input.lower())

    words = {}

    for line in dictionary:
        words[line.lower()] = sort_word(line).lower()
    
    results = append_results(words, sorted_input)  

    for result in results:
        print result
            

if __name__ == "__main__":
    main(sys.argv[1])
