# Def python prompting for varios load sizes
# file is to be imported so this file will contain functions

def get_input_size():
    # function that prompts for user input
    # return a list of viable options
    optional_test_sizes = [2000, 10000, 50000, 100000]
    # prompt user; tell all sizes and have choose numerically
    # error check
    # return array size
    return list(range(1, optional_test_sizes[0]+1))

def check_time():
    # get the time before and after the test is ran to compare how long it took
    # !!this time is not BIG O but is the time the hardware took to run the test!
    # return time.now()
    pass

# note this may be ran on multiple operating systems thus OS imports may need to be checked for OS type.
