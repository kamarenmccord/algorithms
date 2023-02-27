# Test file for all things linear
import test_loader
from time import sleep
from os import system, name
from globals import *

def clear():
    system("cls" if name == "nt" else "clear")

def exit_function():
    #print text to screen
    # pause for a second for the user to read
    # exit program
    exit()

def execute_algo(algo_numb):
    # Main vars
    algo_numb -=1
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
    ALGORITHM_OPTIONS[algo_numb]["function"](test_data)

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

def check_exit():
    """ replaces the input prompt to check for any exit words then passes input back """
    keywords = input("> ")
    if keywords.lower() in EXIT_WORDS:
        exit_function()
    return keywords

def print_avaliable_algorithms():
    for numb, item in enumerate(ALGORITHM_OPTIONS, 1):
        name = item["name"]
        print(f"{numb}) {name}")

def do_greeting():
    # clear the screen
    clear()
    print("\n\n\n")
    # print out a friendly hello
    print("hello wolrd")
    # give some information
    print("This is what the program can do, heres some help information")
    # ascii art mabye
    print("""
      ฅ/ᐠ. ̫ .ᐟ\ฅ < Meow""")
    print("========================")
    # prompt to hit enter to begin (basic input will do, wont be saved)
    print("press enter to continue...")
    check_exit()
    clear()

do_greeting()
while True:
    # print entry data / option info
    print("Enter an option to test the algorithm:")
    print_avaliable_algorithms()
    user_option = check_exit()
    try:
        user_option = int(user_option)
        if user_option <= len(ALGORITHM_OPTIONS) and user_option > 0:
            execute_algo(user_option)
        else:
            print("this option is not avaliable")
    except ValueError:
        print("there has been an error with your input.\nTry again!!")
 
    sleep(CLEAR_SPEED)
    clear()
