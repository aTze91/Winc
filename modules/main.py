# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
# import this
import time
import math
from datetime import datetime as dt
import sys
import greet


def wait(seconds):
    time.sleep(seconds)
    return None


def my_sin(x):
    return math.sin(x)


def iso_now():
    return dt.now().isoformat(timespec='minutes')


def platform():
    return sys.platform.lower()


def supergreeting_wrapper(name):
    return greet.supergreeting(name)
