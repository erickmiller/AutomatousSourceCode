#!/usr/bin/python
__author__ = 'Erick Miller for Stanford CS221'


"""
Example that trains an LSTM based recurrent network and draws samples
from the network using character-level parsing.

Reference:
    Generating sequences with recurrent neural networks `[Graves2014]`_
.. _[Graves2014]: http://arxiv.org/pdf/1308.0850.pdf
"""

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
args = parser.parse_args(gen_be=False)

# Override save path if None
if args.save_path is None:
    args.save_path = 'rnn_code_gen.pickle'

if args.callback_args['save_path'] is None:
    args.callback_args['save_path'] = args.save_path

if args.callback_args['serialize'] is None:
    args.callback_args['serialize'] = 1000

# hyperparameters
args.batch_size = 64
time_steps = 128
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

# model initialization
layers = [
    LSTM(hidden_size, init, activation=Logistic(), gate_activation=Tanh()),
    LSTM(hidden_size, init, activation=Logistic(), gate_activation=Tanh()),
    Affine(len(train_set.vocab), init, bias=init, activation=Softmax())
]
model = Model(layers=layers)

cost = GeneralizedCost(costfunc=CrossEntropyMulti(usebits=True))

optimizer = RMSProp(gradient_clip_value=gradient_clip_value, stochastic_round=args.rounding)

# configure callbacks
callbacks = Callbacks(model, train_set, eval_set=valid_set, **args.callback_args)

# fit and validate
model.fit(train_set, optimizer=optimizer, num_epochs=args.epochs, cost=cost, callbacks=callbacks)


