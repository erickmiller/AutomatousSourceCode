#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sortedDictValue(adict):
    keys = adict.keys()
    keys.sort()
    return [(key,adict[key]) for key in keys]

def test_sortedDictValue():
    adict = { 'a':1,
              'c':22,
              'b':5 }
    
    print adict
    print sortedDictValue(adict)


def case_insensitive(string_list):
    auxiliary_list = [ (x.lower(), x) for x in string_list ]
    auxiliary_list.sort()
    return [ x[1] for x in auxiliary_list ]


def test_case_insensitive():
    sample_list = ['natsuko',
                   'SATOSHI',
                   'YOHKO',
                   'masahito']
    
    print sample_list
    print case_insensitive(sample_list)
    
    # python 2.4 or later
    print sorted(sample_list, key=str.lower)

def main():
    test_sortedDictValue()
    test_case_insensitive()

if __name__ == '__main__':
    main()
