#!/usr/bin/python
__author__ = 'Erick Miller for Stanford CS221'

from collections import OrderedDict
from bs4 import BeautifulSoup
import subprocess
import logging
import urllib2
import random
import time
import uuid
import os

import sys, argparse, getpass
_usage_statement_ = """

shell use:

    python %s -num_pages [int] -term_search [string] -save_dir [/local/path/]

    required flags:

        -num_pages      total number of github.com pages to scrape
                        each page scrape grabs ~10 python files
                        minimum value is 1, maximum value is 100

        -term_search    whitespace delimited string of search terms
                        this script was made to find function definitions
                        so it adds the search terms def (and) return

        -save_dir       this a FULL path to somewhere locally on your
                        computer or on your computer network (like your
                        home directory) - directory MUST EXIST ALREADY
                        also, be sure to make a new folder, this script
                        downloads lots and lots of data and will
                        be sure to overcrowd any directory if you
                        already have files in there

example:

    python %s -num_pages 100 -term_search "square root" -save_dir "/home/%s/data/myfolder/"

""" % (sys.argv[0], sys.argv[0], getpass.getuser())


class GitHubScraper:
    """
    GitHubScraper class contains all the code needed
    to scrape GitHub for the python code gathered and
    used to train the generative neural network models that
    are used to generate code snippets
    """

    def __init__(self):
        # thisfixes a known ssl crashing issue on ubuntu I'm running into
        # when github close a connection and default TLS 1.1 negotiation used
        # so, use the old version instead with this "monkey patch" lol
        import ssl
        from functools import wraps
        def sslwrap(func):
            @wraps(func)
            def bar(*args, **kw):
                kw['ssl_version'] = ssl.PROTOCOL_TLSv1
                return func(*args, **kw)
            return bar
        ssl.wrap_socket = sslwrap(ssl.wrap_socket)


    def downloadTheCode(self, whereToSaveCodePath, githubRelativeUrlList ):
        """
        The code downloader part of the scraper, printing
        various helpful shell status msgs along the way
        """
        if not whereToSaveCodePath.endswith("/"):
            whereToSaveCodePath = whereToSaveCodePath+"/"

        for relpath in githubRelativeUrlList :
            url = "https://raw.github.com" + ("/".join( [ part for part in relpath.split("/") if part != "blob" ] ) )
            print "Scraping file:\n", url
            opener = urllib2.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            u  = opener.open(url)
            meta = u.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            print "Downloading: %s Bytes: %s" % (url.split("/")[-1], file_size)

            file_name = (whereToSaveCodePath+str(uuid.uuid4())+"__"+url.split("/")[-1])
            f = open(file_name, 'w')

            file_size_dl = 0
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break

                file_size_dl += len(buffer)
                f.write(buffer)
                status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
                status = status + chr(8)*(len(status)+1)
                print status,

            f.close()
            u.close()
            time.sleep(random.randint(1,3))


    def saveCodeUrlList(self, whereToSaveUrlListPath, code_page_links, prefix ):
        """
        Save the URLs we just scraped for attribution and so we can browse &
        re-download the orig source files again some time if ever needed
        """
        if not whereToSaveUrlListPath.endswith("/"):
            whereToSaveUrlListPath = whereToSaveUrlListPath+"/"

        #remove duplicates, incase (and) b/c there were duplicates
        rel_code_paths = list(OrderedDict.fromkeys(code_page_links))

        url_list_file = open(whereToSaveUrlListPath + prefix+"__scraped_url_list.txt", "w")
        for relpath in rel_code_paths:
            url_list_file.write( relpath+"\n" )
        url_list_file.close()


    def scrapeGitHubForCode(self, github_search_terms, num_pages_to_scrape, local_path_to_save_code_files ):
        """
        This is the main web scraping code. Had to do way more work to
        fight against Git Hub's rate limiting and throttling mechanisms
        which makes this code run much longer than it would if it was
        unbounded, but anyway it works pretty reliably and I think I
        circumvented all the rate limits and trick Git Hub as much as is needed
        using random numbers to vary the frequency that the code is downloaded...

        ...and an epic git-hub rate-limit rap-battle of history... that i won! :)
        """
        search_terms = 'def+%28+%2C+%29+%3A+return+'+'+'.join(github_search_terms.split())
        code_page_links = []
        page_num = 1
        total_code_scraped = 0

        # Search for and gather up all the URLS first
        # using while loop with exceptions for persistence
        #
        while page_num <= num_pages_to_scrape:

            # more trying to avoid getting ip banned
            # and/or throttled by github (dis iz painful)
            try:
                url = "https://github.com/search?l=python&type=Code&extension:py&p="+str(page_num)+"&q="+search_terms
                print "\n\n***********************\nExecuting new GitHub python code search query:\n", url, "\n"

                opener = urllib2.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                response = opener.open(url)
                page = response.read()
                soup = BeautifulSoup(page)

                code_results_div = soup.findAll('div',attrs={'id':'code_search_results'})
                download_these_files_now = []
                for div in code_results_div:
                    links = div.findAll('a')
                    for link in links:
                        href_loc = link.get('href')
                        if( href_loc.endswith(".py") and link.text.endswith(".py") ):
                            code_page_links.append( href_loc )
                            download_these_files_now.append( href_loc )

                rel_code_paths = list(OrderedDict.fromkeys(download_these_files_now))

                # download the individual python files
                # oh my goodness github you are a pain
                # to scrape, stop rate limiting me....
                #
                count=0
                while count != len(rel_code_paths):
                        try:
                            print "\n\nAttempting to fetch: ", rel_code_paths[count]
                            self.downloadTheCode( local_path_to_save_code_files, [ rel_code_paths[count] ] )
                            count = count +1
                        except urllib2.HTTPError, errr:
                            if( errr.code == 400 ):
                                # someone must have used .py in a link that did not
                                # contain a python file uh, why would they do that?
                                # github server says this file doesn't exist...
                                # anyway i guess they would know better than me.
                                # anyway, skip this one for now, it doesn't exist
                                count = count +1
                                logging.error(errr)
                                print "Error Code: ", errr.code, " File doesn't exist.  Skipping this bogus URL..."
                            else:
                                logging.error(errr)
                                pausetime = random.randint(14,38)
                                print "Error Code: ", errr.code, " PAUSING FOR ", str(pausetime), " seconds. Rate limits?"
                                time.sleep(pausetime)

                page_num = page_num + 1
                total_code_scraped = total_code_scraped + len(rel_code_paths)
                print "\n\n\n*******\nINFO: So far scraped ", total_code_scraped , " URLS..."
                response.close()
                opener.close()

            except urllib2.HTTPError, err:
                logging.error(err)
                pausetime = random.randint(11,33)
                print ("PAUSING FOR "+str(pausetime)+" seconds.  GIT HUB IS RATE LIMITING? ")
                time.sleep(pausetime)

            # keep looking natural ;) and avoid getting ip banned
            pausetime = random.randint(3,7)
            print ("\n\n\n*******\nINFO: Pausing for "+str(pausetime)+" secs to avoid rate limits.")
            time.sleep(pausetime)

        # in case we want to download again later, also for referring to original:
        save_paths_for_later = list(OrderedDict.fromkeys(code_page_links))
        self.saveCodeUrlList( local_path_to_save_code_files, save_paths_for_later, "_".join(github_search_terms.split()) )

        if not local_path_to_save_code_files.endswith("/"):
            local_path_to_save_code_files = local_path_to_save_code_files+"/"

        merged_data_filename = "ALL_" + ("_".join(github_search_terms.split()).upper()) + "_TRAINING_DATA.txt"

        cmd = 'for i in {} ; do cat $i ; echo "" ; done > {} 2>&1'.format( local_path_to_save_code_files+"*.py", local_path_to_save_code_files+merged_data_filename  )

        output = subprocess.check_output( '{} | tee /dev/stderr'.format( cmd ), shell = True )

        if os.path.exists(local_path_to_save_code_files+merged_data_filename):
            print "\n\n********************************\n"
            print "\nSAVED MERGED CODE INTO ONE BIG FILE FOR FEATURE EXTRACTION:\n"
            print local_path_to_save_code_files+merged_data_filename
            print "\n\n********************************\n\n"

        print "\nScraping is completed for search term: ", github_search_terms, "\n"


 ##################
  #GitHubScraper#
   #############
     #########
      #####
        ###
          #
           #

#           h
#          t  u
#        i      b
#     g             c
#                       o   d    e
######################################

# Note to self:
#
# This github developer id token is for
# using github API if they keep giving
# me grief while scraping, I will try
# using their API with this key:
#   9d404f2ab14cce5fe1011ca09478cdf79cbdb105

def main(argv):
    if len(argv) <= 1:
        print _usage_statement_
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description=_usage_statement_)
    parser.add_argument('-num_pages', type=int, help='the number of github pages to scrape.', required=True)
    parser.add_argument('-term_search', help='the words used to search github code', required=True)
    parser.add_argument('-save_dir', help='the local directory where the scraped code will be saved', required=True)
    args = vars(parser.parse_args())
    term_search = args['term_search']
    num_pages = args['num_pages']
    save_dir = args['save_dir']
    if save_dir and term_search and num_pages:
        if num_pages > 100:
            num_pages = 100
        if num_pages < 1:
            num_pages = 1
        is_directory = os.path.isdir(save_dir)
        path_exists = os.path.exists(save_dir)
        if not is_directory or not path_exists:
            print """
            ERROR:  %s   DOES NOT EXIST.

            The path sent to -save_dir must EXIST ALREADY.
            It is highly suggested that you make a new directory
            to save all of your scraped data into if you are attempting
            to use this script because it creates lots of files.
            """ % save_dir
            exit()
        else:
            scraper = GitHubScraper()
            scraper.scrapeGitHubForCode( term_search, num_pages, save_dir  )
    else:
        print _usage_statement_
    pass

if __name__ == "__main__":
    main(sys.argv)
