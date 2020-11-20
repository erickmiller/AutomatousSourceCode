from sys import argv

scriptname, filename = argv[0], argv[1]

def create_dictionary(filename):

    input_file = open(filename)

    dictionary = {}

    for line in input_file:
        line = line.rstrip().split(':')
        key, value = line[0], int(line[1])
        dictionary[key] = value

    return dictionary

def sort_dictionary_keys(dictionary):
    sorted_keys = sorted(dictionary.keys())
    return sorted_keys

def print_sorted_dictionary(dictionary, sorted_keys):
    for key in sorted_keys:
        print "Restaurant %r is rated at %d." % (key, dictionary[key])

def main():
    dictionary = create_dictionary(filename)
    sorted_keys = sort_dictionary_keys(dictionary)
    print_sorted_dictionary(dictionary, sorted_keys)


if __name__ == '__main__':
    main()