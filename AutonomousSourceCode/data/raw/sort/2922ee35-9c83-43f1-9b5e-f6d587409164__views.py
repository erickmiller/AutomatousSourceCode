from django.shortcuts import render
from __init__ import pyro


def get_test():
    print library.test()


def home(request, by_what='tytul'):
    """ Strona glowna. Parametr 'by_what' mowi nam po czym sortujemy liste. """

    sort = by_what
    
    book_list = pyro.library.getBook_list(20)
    sorted_list = pyro.library.getBook_sort(by_what, 'ASC', 20)

    template = "index.html"
    context = {'book_list':book_list, 'sorted_list':sorted_list, 'sort':sort}

    return render(request, template, context)
