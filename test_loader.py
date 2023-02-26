# Def python prompting for varios load sizes
# file is to be imported so this file will contain functions
from random import randint

def get_input_size():
    # function that prompts for user input
    # return a list of viable options
    optional_test_sizes = [2000, 10000, 50000, 100000]
    # prompt user; tell all sizes and have choose numerically
    # error check

    unsorted_data = []
    for _ in range(optional_test_sizes[0]):
        unsorted_data.append(randint(1, 100000))
    return unsorted_data

def check_time():
    # get the time before and after the test is ran to compare how long it took
    # !!this time is not BIG O but is the time the hardware took to run the test!
    # return time.now()
    pass

def integrity_check(sortedArray):
    # checks a single dimensional array for numbers that are out of order
    currentNumb=0
    for data in sortedArray:
        if data < currentNumb:
            return False
        currentNumb=data
    return True
        

# note this may be ran on multiple operating systems thus OS imports may need to be checked for OS type.
