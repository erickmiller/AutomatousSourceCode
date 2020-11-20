#!/usr/bin/env python

import math
import time


def findroot(anum):
    """
    Find square root of a number
    """
    try:
        time.sleep(10)
        return math.sqrt(anum)
    except TypeError:
        return 'Not a number'
    except ValueError:
        return 'Value error'
    except KeyboardInterrupt:
        return 'keyboard interrupt error occurred'


def main():
    """
    main method
    """
    print findroot(9)

if __name__ == '__main__':
    main()
