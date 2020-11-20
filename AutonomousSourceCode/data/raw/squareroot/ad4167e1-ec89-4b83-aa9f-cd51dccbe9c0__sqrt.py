# sqrt.py (c) Mikhail Mezyakov <mihail265@gmail.com>
# Released under the GNU GPL v.3
# 
# Returns square root of the input int

from math import sqrt


def horo(channel, user, args):
    """Calculate square root. Usage: sqrt <number>"""

    result = sqrt(int(args[0]))

    return u'PRIVMSG {channel} :{result}'.format(user=user, result=result)
