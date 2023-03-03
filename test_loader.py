# Def python prompting for varios load sizes
# file is to be imported so this file will contain functions
from random import randint
import time
from logic_file import get_input_size
from globals import *

def try_for_int(expected_numb):
    try:
        return int(expected_numb)
    except ValueError:
        print("There has been an error with your input.\nThe input is not an option or contains incorrect matching\nTry again!!")

def check_time():
    # get the time before and after the test is ran to compare how long it took
    # !!this time is not BIG O but is the time the hardware took to run the test!
    return time.time()

def time_calc(start_time, end_time, load_size=0):
    time_taken = end_time - start_time
    return f'The Algorithm on this hardware took:\n{time_taken}ms\n{load_size} entities processed'

def integrity_check(sortedArray):
    # checks a single dimensional array for numbers that are out of order
    # only checks each number after the next and not 1st againt all then 2nd against all
    first_numb=0
    passing_grade=True
    for data in sortedArray:
        if data < first_numb:
            print(f'INTEGRITY CHECK FAILED THIS SORT IS BROKEN:\n{first_numb} is larger than {data}\n')
            passing_grade=False
        first_numb=data

    print(f'Integrity test passed: {passing_grade}')
    if not passing_grade:
        print(sortedArray[:25])
        return False
    passing_grade=True
    return True

def execute_algo(algo_numb):
    algo_numb -=1
    start_time, end_time = 0, 0
    # Get input size before mesuring the time
    test_data = get_input_size()

    # time before the program ran
    start_time = check_time()

    # run an algo
    ALGORITHM_OPTIONS[algo_numb]["function"](test_data)

    # get time after running
    end_time = check_time()

    #test the integrity of the sort
    if not OPTIONS["INTEGRITY_SKIP"]:
        integrity_check(test_data)

    # print how long it took to sort
    print(time_calc(start_time, end_time, len(test_data)))
    # simple pause for a chance to read output
    if not OPTIONS["FULL_AUTO"]:
        input("-= enter to continue =-")
