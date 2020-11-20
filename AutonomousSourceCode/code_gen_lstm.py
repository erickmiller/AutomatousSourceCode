#!/usr/bin/python
__author__ = 'Erick Miller for Stanford CS221'

"""
Draws samples from trained LSTM network

Reference:
    Generating sequences with recurrent neural networks `[Graves2014]`_
.. _[Graves2014]: http://arxiv.org/pdf/1308.0850.pdf
"""


import sys

import numpy as np

from neon.backends import gen_backend
from neon.data import Text
from neon.data import load_text
from neon.initializers import Uniform
from neon.layers import GeneralizedCost, LSTM, Affine
from neon.models import Model
from neon.optimizers import RMSProp
from neon.transforms import Logistic, Tanh, Softmax, CrossEntropyMulti
from neon.callbacks.callbacks import Callbacks
from neon.util.argparser import NeonArgparser, extract_valid_args

# parse the command line arguments
parser = NeonArgparser(__doc__)

parser.add_argument('-st', '--sample_primer_text', default='',
                    help='optional text used as primer to sample deep lstm RNN' )

parser.add_argument('-ns', '--number_of_samples', type=int, default=10,
                    help='used with the st flag to determine number of samples')

args = parser.parse_args(gen_be=False)

# Override save path if None
if args.save_path is None:
    args.save_path = 'rnn_code_gen.pickle'

if args.callback_args['save_path'] is None:
    args.callback_args['save_path'] = args.save_path

if args.callback_args['serialize'] is None:
    args.callback_args['serialize'] = 500

# hyperparameters
args.batch_size = 64
time_steps = 64
hidden_size = 256
gradient_clip_value = 5

# setup backend
be = gen_backend(**extract_valid_args(args, gen_backend))

#data_path = "/shared/StanfordAi/project/data/helloworld.py"
#data_path = "/home/etron/CODE/project/extended_ascii_training_set.txt"
#data_path = "/home/etron/CODE/project/demons_asciiart_training_set.txt"
#data_path = "/home/etron/CODE/project/Demon_and_Bunny.txt"
#data_path = "/home/etron/CODE/project/knowledge_parsed.txt"

data_path = "/home/emill/CODE/project/SCRAPED_GITHUB_DATA/sort/CLEANED__ALL_SORT_TRAINING_DATA.txt"


train_path, valid_path = Text.create_valid_file(data_path)

# load data and parse on character-level
train_set = Text(time_steps, train_path)
valid_set = Text(time_steps, valid_path, vocab=train_set.vocab)

# weight initialization
init = Uniform(low=-0.07, high=0.08)

def sample(prob):
    """
    Sample index from probability distribution
    """
    prob = prob / (prob.sum() + 1e-6)
    return np.argmax(np.random.multinomial(1, prob, 1))


####
# Set batch size and time_steps to 1 for generation and reset buffers
# then load up the pickle file with the saved model and weights
#
be.bsz = 1
time_steps = 1
num_predict = args.number_of_samples

layers = [
    LSTM(hidden_size, init, activation=Logistic(), gate_activation=Tanh()),
    LSTM(hidden_size, init, activation=Logistic(), gate_activation=Tanh()),
    Affine(len(train_set.vocab), init, bias=init, activation=Softmax())
]
model_new = Model(layers=layers)
model_new.load_weights(args.save_path)
model_new.initialize(dataset=(train_set.shape[0], time_steps))


####
# Generative RNN sample time!
#
text = []
seed_tokens = list( args.sample_primer_text )

x = be.zeros((len(train_set.vocab), time_steps))

for s in seed_tokens:
    x.fill(0)
    x[train_set.token_to_index[s], 0] = 1
    y = model_new.fprop(x)

for i in range(num_predict):
    # Take last prediction and feed into next one
    pred = sample(y.get()[:, -1])
    text.append(train_set.index_to_token[int(pred)])

    x.fill(0)
    x[int(pred), 0] = 1
    y = model_new.fprop(x)

print ''.join(seed_tokens + text)
