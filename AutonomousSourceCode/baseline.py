#!/usr/bin/python
__author__ = 'Erick Miller for Stanford CS221'

import scraper
import features
import random
import os.path


"""

This is a super simple baseline algorithm to
replicate current human behavior, it basically
searches github for the search term,
and then randomly returns one python function
that was found.

This is appears to be a relatively
accurate representation of a basic
result that can be improved upon,
especially since this is the same data that
we run learning algorithm on (only with much more data)

"""


save_dir = "/home/emill/CODE/project/data/baseline/sqrt/"

term_search = "square root"
num_pages = 1

filename = "ALL_SQUARE_ROOT_TRAINING_DATA.txt"


if os.path.exists(save_dir):

    if not os.path.isfile(save_dir+filename):
        gitscrape = scraper.GitHubScraper()
        gitscrape.scrapeGitHubForCode( term_search, num_pages, save_dir  )
    else:
        phi = features.Features(save_dir+filename)
        cleaned_code = phi.stripComments()
        functions = phi.parseFunctions( cleaned_code )

        if len(functions):
            random.shuffle( functions )
            print functions[0]
        else:
            print "\n\n\nTHE BASELINE ALGORITHM DID NOT FIND A REASONABLE BASELINE!\n\n"

else:
    print "ERROR: ", save_dir, "  DOES NOT EXIST... change the path in the baseline script..."