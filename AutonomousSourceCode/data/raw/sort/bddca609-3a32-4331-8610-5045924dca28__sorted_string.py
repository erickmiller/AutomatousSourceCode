#   Conor T. Ryan
#   Week 5 Homework
#   UW PCE Programming in Python
#   Fall 2011 (Jacky)

def sorted_string(stringToSort):

    # conv string into list and alphabetize
    sortedList = list(stringToSort)
    sortedList.sort()

    # conv list back into string
    result = ''.join(sortedList)

    return result

if __name__ == '__main__':

    string1 = 'hello'
    string2 = 'teststring'
    
    print sorted_string(string1)
    print sorted_string(string2)
