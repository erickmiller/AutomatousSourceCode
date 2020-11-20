store = []

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(strings, key=last_letter)