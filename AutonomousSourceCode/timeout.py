#!/usr/bin/python
__author__ = 'Erick Miller for Stanford CS221'

"""
This is a quick implementation based on a suggestion from
Stack Overflow user David Narayan to use signal handling
in python to handle executing functions that might time out.

This problem came up during the project several times both
while scraping code and while processing some malformed code.

The basic idea is to use signal handlers to set an alarm for
some time interval and raise an exception once that timer expires.
Apparently this only works on Linux or Unix systems.

This code creates a decorator called @timeout that can be applied
to any long running functions.

Usage: In the application code, this is used as a decorator:

from timeout import timeout

@timeout(7)
def long_running_function():

"""

from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator