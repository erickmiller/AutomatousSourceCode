#!/usr/bin/env python
""" Example run of the pythonREST server

To test, run this script (either python example_server.py or
as an executable ./python), and in a seperate terminal
call, for example (square root of 10):

curl -X POST http://0.0.0.0:9090 -d '{"fun":"root_fun", "params":{"n" : 10}}'

Or, in a seperate terminal, execute the example_client.py file.
"""

import math
import time

import pythonrest

def square_fun(params):
    """
    Square the scalar input
    """
    return {"value": params["n"]**2}

def root_fun(params):
    """
    Find the root of the scalar input
    """
    return {"value": math.sqrt(params["n"])}

def one_plus_inverse(params):
    if params["n"] == 0:
        return {"value": None}
    else:
        return {"value": 1.0 + 1.0/params["n"]}

def wait_5_secs(params):
    time.sleep(5)
    return {"value": 1}

pyserver = pythonrest.PyServer()
pyserver.add_post_fun(square_fun)
pyserver.add_post_fun(root_fun)
pyserver.add_post_fun(one_plus_inverse)
pyserver.add_post_fun(wait_5_secs)
pyserver.run()

