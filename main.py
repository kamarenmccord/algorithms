""" Main file that runs the rest of the program, only frontend logic is here """
import test_loader
from time import sleep
from globals import *
from test_loader import execute_algo
from logic_file import (
    clear, do_greeting, print_avaliable_algorithms,
    check_exit, show_settings, show_help, get_option,
)

do_greeting()
while True:
    # print entry data / option info
    print("Enter a number to begin or help for help:")
    print_avaliable_algorithms()

    user_option = check_exit(skip_line=False)
    # check to see if asking for options or help
    if user_option.lower() in SETTINGS_KEYWORDS:
        show_settings()
    if user_option.lower() in HELP_KEYWORDS:
        show_help()

    # run the program as expected
    else:
        user_option = test_loader.try_for_int(user_option)
        if user_option:
            if user_option <= len(ALGORITHM_OPTIONS) and user_option > 0:
                execute_algo(user_option)
        else:
            print("You must enter something...")
 
    sleep(get_option("CLEAR_SPEED"))
    clear()
