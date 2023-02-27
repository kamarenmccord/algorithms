# Test file for all things linear
import test_loader
from buble_sort import bubble_sort

# main variables
loop_switch = True

algorithm_options = [
    "bubble_sort",
]

exit_words = [
    "quit", "exit", "end", "stop",
]

def exit_function():
    #print text to screen
    # pause for a second for the user to read
    # exit program
    exit()

def execute_algo():
    # Main vars
    # integrity test skip
    """
    should only be used for testing 
    this may take an exessive amount of time 
    the integrity test can double the time or worse 
    like: O(!) then linear searching (test) 100,000 entities!!
    """
    integrity_skip = False
    start_time, end_time = 0, 0
    # Get input size before mesuring the time
    test_data = test_loader.get_input_size()

    # time before the program ran
    start_time = test_loader.check_time()
    # run an algo
    bubble_sort(test_data)
    # get time after running
    end_time = test_loader.check_time()

    #test the integrity of the sort
    if not integrity_skip:
        test_passed = test_loader.integrity_check(test_data)
        print(f'Integrity test passed: {test_passed}')
        if test_passed == False:
            print(test_data[:25])

    # print how long it took to sort
    print(test_loader.time_calc(start_time, end_time, len(test_data)))

def get_input():
    print("enter something here:")
    return input("> ")

### TODO
# print greeting to program and explain what does

while loop_switch:
    # print entry data / option info
    # ask for input to stop loop
    user_option = get_input()
    # check input for false condition
    if user_option in exit_words:
        loop_switch = False
        exit_function()
    else:
        # create end condition
        execute_algo()
