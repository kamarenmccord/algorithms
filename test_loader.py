"""
Contains functions for checking the integrity 
of sorts and how long a test took to run
"""
import time
from logic_file import get_input_size, try_for_int
from globals import *
from logic_file import clear, get_target

# Time
def check_time():
    # get the time before and after the test is ran to compare how long it took
    # !!this time is not BIG O but is the time the hardware took to run the test!
    return time.time()

def time_calc(start_time, end_time, load_size=0):
    time_taken = end_time - start_time
    seconds=False
    if time_taken > 1000:
        time_taken = time_taken/1000
        seconds=True
    if seconds:
        return f"The Algorithm on this hardware took:\n{time_taken}Seconds\n{load_size} entities processed"
    return f'The Algorithm on this hardware took:\n{time_taken}ms\n{load_size} entities processed'

def execute_algo(algo_numb):
    algo_numb -= 1
    target_number= 1
    algo_name = ALGORITHM_OPTIONS[algo_numb]["function"]

    # check to see if this is a search or sort
    if ALGORITHM_OPTIONS[algo_numb]["search"]:
        test_data = get_input_size(sorted=True)
        target_number = get_target(len(test_data))
    else:
        test_data = get_input_size()

    start_time, end_time = 0, 0

    clear()
    print("The Algorithm is running, please wait...")
    start_time = check_time()  # time before the program ran
    #!! run an algo
    if not ALGORITHM_OPTIONS[algo_numb]["search"]:
        algo_name(test_data)  # this is a sort
    else:
        algo_name(test_data, target_number)  # this is a search
    end_time = check_time()  # get time after running

    #test the integrity of the sort
    if not OPTIONS["INTEGRITY_SKIP"]:
        integrity_check(test_data)

    # print how long it took to sort
    clear()
    print("results:")
    print(time_calc(start_time, end_time, len(test_data)))
    # simple pause for a chance to read output
    if not OPTIONS["FULL_AUTO"]:
        input("-= enter to continue =-")

# Integrity Test
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
