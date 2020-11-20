def sort_anagram(lst):
    lst_new = [(sorted(s), s) for s in lst]
    lst_new.sort()
    return [t[1] for t in lst_new]

if __name__ == '__main__':
    lst = ['axyz', 'abc', 'yzax', 'bac', 'zyxa', 'fg', 'gf']
    print sort_anagram(lst)
