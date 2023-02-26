# Def python prompting for varios load sizes
# file is to be imported so this file will contain functions
from random import randint
import time

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
    return time.time()

def time_calc(start_time, end_time, load_size=0):
    time_taken = end_time - start_time
    return f'The Algorithm on this hardware took:\n{time_taken}ms\n{load_size} entities processed'

def integrity_check(sortedArray):
    # checks a single dimensional array for numbers that are out of order
    first_numb=0
    for data in sortedArray:
        if data < first_numb:
            print(f'INTEGRITY CHECK FAILED THIS SORT IS BROKEN:\n{first_numb} is larger than {data}\n')
            return False
        first_numb=data
    return True
