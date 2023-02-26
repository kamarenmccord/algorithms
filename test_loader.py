# Def python prompting for varios load sizes
# file is to be imported so this file will contain functions

from random import randint
from time import now
import os

def get_input_size():
    # function that prompts for user input
    # return a list of viable options
    optional_test_sizes = [2000, 10000, 50000, 100000]

def check_time():
    # get the time before and after the test is ran to compare how long it took
    # !!this time is not BIG O but is the time the hardware took to run the test!
    return now()

# note this may be ran on multiple operating systems thus OS imports may need to be checked for OS type.
