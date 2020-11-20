README
_________________________________
DIRECTORY DESCRIPTIONS:

_________________________________
Epoch training data for neural networks:
cv/

_________________________________
Truncated data files included (to not exceed Stanford's 20MB data upload limits)
data/

_________________________________
Lua scripts that are a part of the LSTM RNN library by A. Karpthy:
model/

_________________________________
Utility scripts as part of the RNN library:
util/


_________________________________
FILE DESCRIPTIONS:


_________________________________
A. Karpathy's RNN library using sliding windows sequence learning with one-hot vectors feature extraction
In Lua / Torch --  these are the scripts use to train the RNNs described in final.pdf and more information can
be found here:   https://github.com/karpathy/char-rnn

THE DATA USED TO TRAIN THE MODELS DESCRIBED IN FINAL.PDF IS INCLUDED IN THE data/ directory
So everything needed to recreate the examples in the report is included here in the directory
(ASSUMING ALL SOFTWARE DEPENDENCIES ARE INSTALLED) and there are alot of software dependencies

	inspect_checkpoint.lua*
	sample.lua*
	train.lua*


_________________________________
THIS IS THE MAIN SCRIPT USED TO TRIGGER THE MAIN ALGORITHM DESCRIBED 
IN THE FINAL.PDF REPORT.  PLEASE EXCUSE CODE SLOP AS TIME WAS AN
IMMOVABLE CONSTRAINT WHILE FINISHING THIS PROJECT!  
	code_creator.py*

THIS SCRIPT DOES NOT HAVE COMMAND LINE ARGUMENTS, AS I RAN OUT OF TIME,
TO RUN THIS SCRIPT, SIMPLY OPEN IT IN AN EDITOR, SCROLL DOWN,
AND MODIFY THESE VARIABLES:

	Definition = '"def double( num ):"'

	InputExample= 512

	CorrectAnswer = 1024

	TrainedWeights = "cv/lm_lstm_epoch50.00_0.6677.t7"


_________________________________
THIS IS A SCRIPT I USED WHILE EXPERIMENTING WITH A VARIETY
OF OTHER NEURAL NETWORK MODELS USING THE NEON LIBRARY

THIS SCRIPT IS NOT REFINED, BUT EASILY HACKABLE 
AND IS USED FOR SAMPLING FROM THE NEURAL MODELS

	code_gen_lstm.py*



_________________________________
FEATURE EXTRACTOR AS DESCRIBED IN FINAL.PDF
THIS CODE IS PARTIALLY REFINED BUT NOT FULLY REFINED
AS TIME RAN OUT TOWARDS THE DEADLINE. 
WHILE THIS CODE IS INCOMPLETE, 
IT IS NICELY PACKAGED INTO A CLASS AND RELATIVELY BUG FREE

	features.py



_________________________________
THIS IS THE WEBSCRAPER DESCRIBED IN FINAL.PDF

shell use:

    python scraper.py -num_pages [int] -term_search [string] -save_dir [/local/path/]

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

    python scraper.py -num_pages 100 -term_search "square root" -save_dir "/home/emill/data/myfolder/"


usage: scraper.py [-h] -num_pages NUM_PAGES -term_search TERM_SEARCH -save_dir
                  SAVE_DIR
scraper.py: error: argument -num_pages is required


scraper.py*



_________________________________
GREAT UTILITY CLASS FOR CREATING DECORATORS THAT ALLOW YOU TO
AVOID INFINTE OR REALLY LONG RUNNING PYTHON FUNCTIONS 

	timeout.py



_________________________________
THIS IS THE SCRIPT I USED WHILE EXPERIMENTING WITH A VARIETY
OF OTHER NEURAL NETWORK MODELS USING THE NEON LIBRARY

THIS SCRIPT IS NOT REFINED, BUT EASILY HACKABLE 
AND IS USED FOR TRAINIG THE NEURAL MODELS


	code_gen_train_lstm.py*

_________________________________
THIS IS THE DEFAULT FILE CREATED FOR SAVING THE COEFICIENTS 
FROM NEON'S NEURAL NETWORK MODELS FROM MY SCRIPT
THAT USES THE NEON LIBRARY, IF NO ARGUMENT IS SUPPLIED

	rnn_code_gen.pickle*



_________________________________
Library I wrote / collected for deriving more effective meaning from python Abstract Syntax Trees:
astutils.py

_________________________________
The script to generate baseline examples. Open the script and change the following variables:

	save_dir = "/home/emill/CODE/project/data/baseline/sqrt/"
	term_search = "square root"
	num_pages = 1
	filename = "ALL_SQUARE_ROOT_TRAINING_DATA.txt"

baseline.py

_________________________________
THIS ONE OF THE SCRIPTS I USED WHILE EXPERIMENTING WIHT LATENT DIRLICT ALLOCATION KNOWLEDGE CLUSTERING 
ON STACK OVERFLOW DATA

knowledge_extractor.py*



_________________________________
FULL UNABRIDEGED OUTPUT FROM SHELL FOR ALL DETAILS OF RESULTS OUTPUT AS DESCRIBED IN FINAL.PDF

double_ouput_log.txt
half_ouput_log.txt
squared_ouput_log.txt
square_root_ouput_log.txt





