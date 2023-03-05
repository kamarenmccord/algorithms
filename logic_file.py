""" Main Logic File, main loop functions """
from os import system, name
from globals import *
from random import randint
from time import sleep

# global vars
sleep_time = OPTIONS["CLEAR_SPEED"]

#helper functions
def clear():
    # clears the screen on either windows or bash systems
    system("cls" if name == "nt" else "clear")
    
def new_line(numb=1):
    # just prints a empty line out to give variable spacing
    # numb will be the count of lines it will print spacing for
    for _ in range(numb):
        print()

# messages / intro / extros
def exit_function():
    # runs on exit, gives user closure
    clear()
    new_line()
    print(EXIT_MESSAGE)
    input("-=Press enter to LEAVE=-\n\n")
    clear()
    exit()

def print_avaliable_algorithms():
    for numb, item in enumerate(ALGORITHM_OPTIONS, 1):
        name = item["name"]
        print(f"{numb}) {name}")

def do_greeting():
    # clear the screen
    clear()
    print("\n\n\n")
    # print out a friendly hello
    print("Welcome to the algorithm runner\nThis Program can execute many searches with various input sizes.")
    print("To see how long a search or sort will take choose one from a list and let it run!")
    print("""
      ฅ/ᐠ. ̫ .ᐟ\ฅ < Meow""")
    print("========================")
    print("press enter to continue...")
    check_exit(skip_line=False)
    clear()
    
# Menus
def show_settings():
    # build options 1 time
    optional_list = []
    for option in OPTIONS:
        if option not in FIXED_OPTIONS:
            optional_list.append([option])

    while True:
        # give options
        clear()
        for numb, option in enumerate(optional_list, 1):
            if option not in FIXED_OPTIONS:
                print(f"{numb}) {option}")
        print("You may type end to exit this menu")

        # some way to exit settings
        choice = check_exit(back_out=True)
        if not choice:
            clear()
            print("exiting settings")
            return

        # error check input
        choice = try_for_int(choice)
        choice -= 1
        try:
            choice = OPTIONS[optional_list[choice][0]]
            # get the option to change
            # present options and messages if there is any
            print(choice)
            sleep(sleep_time)
        except:
            print("an error has occured, try again")
            sleep(sleep_time)

# input
def get_target(limit):
    # advanced function defined to return an integer only, will check for exit prompts
    while True:
        clear()
        print(" >Choose a number between< ")
        print(f'1 - {limit}')
        target = check_exit()
        target = try_for_int(target)
        if target:
            if (type(target) == type(6) and target > 0
            and target < limit):
                return target
        else:
            print(" you must choose a number Between the provided range ")
            sleep(sleep_time)

def check_exit(skip_line=True, back_out=False):
    """ replaces the input prompt to check for any exit words then passes input back """
    if skip_line:
        print("\n")
    keywords = input("> ")
    if keywords.lower() in EXIT_WORDS:
        if not back_out:
            exit_function()  # close the app
        return False  # get out the loop
    return keywords  # return input clean, may be other menu or number

def get_input_size(sorted=False):
    # function that prompts for user input
    while True:
        clear()
        print("How many entities would you like to use?")
        for numb, option in enumerate(OPTIONS["TEST_SIZE"], 1):
            print(f"{numb}) {option}")
        choice = check_exit()
        if choice:
            choice = try_for_int(choice)
            if (type(choice) == type(5) and choice-1 >= 0 
            and choice-1 < len(OPTIONS["TEST_SIZE"])):
                data_sample = []
                choice -= 1
                if not sorted:
                    for _ in range(OPTIONS["TEST_SIZE"][choice]):
                        data_sample.append(randint(1, OPTIONS["RANDOM_UPPPER_LIMIT"]))
                    return data_sample
                for n in range(OPTIONS["TEST_SIZE"][choice]):
                    data_sample.append(n)
                return data_sample
            print("this input size is not accepted, try again from the list")
            sleep(sleep_time)

def try_for_int(expected_numb):
    try:
        return int(expected_numb)
    except:
        return ""
