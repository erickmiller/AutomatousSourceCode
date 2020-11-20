#!/usr/bin/env python


def newmark(oldmark):

    """Mr. Arkiletian's mark-boosting function"""

    return 10 * round(oldmark ** 0.5, 0)  # 10 times square root of old mark


while True:
    old = raw_input()
    if old == "":
        break
    print newmark(float(old)), '\n'
