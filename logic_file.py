""" Main Logic File, main loop functions """
from os import system, name
from globals import *
from random import randint
from time import sleep

# global vars
sleep_time = OPTIONS["CLEAR_SPEED"]["OPTION"]

#helper functions
def clear():
    # clears the screen on either windows or bash systems
    system("cls" if name == "nt" else "clear")

def print_s(message, protected=False, slowtype=False, long=False, sleep_add=0, sleep_skip=False, half_step=False, hard_pause=False, head_lines=0, tail_lines=0, screen_clear=False):
    """ Major overhaul on the basic print statement
    @message - required string to print out
    @protected - message cannot be skipped
    @slowtype - invoke the typewritter function
    @long - typewrite quickly
    @sleep_add - add time to sleep timer (for important messages)
    @sleep_skip - skip the sleep timer and move on
    @half_step - print things out in bits but quicker than basic sleep
    @hard_pause - invokes the input command to wait for a enter input
    @head_lines - newlines before
    @tail_lines - newlines after
    @screen_clear - clear the screen
    """
    clear() if screen_clear else False
    if not get_option("SKIP_DIALOGUE") or protected:
        print("\n"*head_lines, end="") if head_lines>0 else False
        if message:
            typewriter(str(message), quick=long) if slowtype else print(message, flush=True)
        print("\n"*tail_lines, end="") if tail_lines>0 else False
        if not sleep_skip:
            sleep(sleep_time+sleep_add)
        if half_step:
            sleep(0.2)
        if hard_pause:
            input("--==={ press enter to continue }===--")
    else:
        pass

def typewriter(word, quick=False):
    for letter in word:
        print(letter, end="", flush=True)
        sleep(0.01 if quick else 0.08)
    print()

def new_line(numb=1):
    # just prints a empty line out to give variable spacing
    # numb will be the count of lines it will print spacing for
    print("\n"*numb)

def get_option(name, type="OPTION"):
    """ returns option values in a simpler way, is more scaleable than modding every interation of the call 
    @name == name of option
    @type == type [OPTION, MESSAGE, SWITCHABLE]
    """
    return OPTIONS[name][type]

def try_for_bool(expeted_phrase):
    expeted_phrase = expeted_phrase.lower()
    if expeted_phrase in ["true", "false"]:
        if expeted_phrase == "true":
            return True
        if expeted_phrase == "false":
            return False
    return expeted_phrase

def try_for_int(expected_numb, index=False):
    try:
        if index == True:
            return int(expected_numb)-1
        return int(expected_numb)
    except:
        return ""

# messages / intro / extros
def exit_function():
    # runs on exit, gives user closure
    print_s(EXIT_MESSAGE, screen_clear=True, head_line=1, protected=True, sleep_skip=True)
    input("-=Press enter to LEAVE=-\n\n")
    clear()
    exit()

def print_avaliable_algorithms():
    for numb, item in enumerate(ALGORITHM_OPTIONS, 1):
        name = item["name"]
        print(f"{numb}) {name}")

def do_greeting():
    print_s(INTRO_MESSAGE, protected=True, slowtype=True, long=True, screen_clear=True, sleep_skip=True)
    check_exit(skip_line=False)
    clear()

# Menus
def show_settings():
    # build options 1 time
    optional_list = []
    for option in OPTIONS:
        if get_option(option, type="SWITCHABLE"):
            optional_list.append([option])

    while True:
        # give options
        clear()
        for numb, option in enumerate(optional_list, 1):
            print_s(f"{numb}) {option[0]} : {get_option(option[0])}",protected=True ,half_step=True, sleep_skip=True, tail_lines=1)
        print("Enter to exit or enter a number to get started")

        # some way to exit settings
        choice = check_exit(back_out=True)
        if not choice:
            print_s("exiting settings", screen_clear=True)
            return False

        # error check input
        choice = try_for_int(choice, index=True)
        try:
            # get all the settings related to the choice, not just one thus no helper
            setting = OPTIONS[optional_list[choice][0]]  # all the data
            setting_message = setting["MESSAGE"]
            setting_value = setting["OPTION"]
            setting_limit_min = ""
            setting_limit_max = ""

            # integer values will have different stats
            if type(setting_value) == type(1): 
                setting_limit_min = setting["MINIMUM"]
                setting_limit_max = setting["MAXIMUM"]
        except:
            print_s("an error has occured, try again", protected=True, screen_clear=True, slowtype=True, long=True)
  
        # change the setting that is selected
        change_setting(optional_list[choice][0], setting_message, setting_value, setting_limit_min, setting_limit_max)

def show_help():
    print_s(HELP_MESSAGE, protected=True, slowtype=True, long=True, clear=True, sleep_skip=True, hard_pause=True, head_lines=2, tail_lines=1)
    clear()

def change_setting(name, message, value, limit_min="", limit_max=""):
                changed = False
                while not changed:
                    # display option info about the option
                    clear()
                    typewriter(str(name).replace("_", " "))
                    typewriter(str(value))
                    if message:
                        print_s(message, protected=True, slowtype=True, long=True, sleep_skip=True, head_lines=2, tail_lines=1)

                    # get adjustment
                    new_value = check_exit(skip_line=False, back_out=True)

                    if not new_value:
                        print_s("Nothing Changed", protected=True, screen_clear=True)
                        return False
                    if new_value:
                        # string checks
                        if new_value.lower() in ["true", "false"] and type(value) == type(False):
                            OPTIONS[name]["OPTION"] = try_for_bool(new_value)
                            changed = True
                        elif type(value) == type(new_value):
                            OPTIONS[name]["OPTION"] = new_value
                            changed=True

                        # integer checks
                        elif (type(value) == type(try_for_int(new_value)) and
                                limit_min >= int(new_value) <= limit_max):
                            OPTIONS[name]["OPTION"] = int(new_value)
                            changed = True
                        
                        if changed:
                            print_s("Value Set", screen_clear=True, slowtype=True, long=True)
                            return
                        else:  # An actual user input happens error
                            print_s(
                            """
                            Value was not accepted,
                            It may be too high or low or the wrong value type
                            check spelling and try again
                            """, sleep_add=2, protected=True)
                    else:
                        print_s("value not is accepted, try again", protected=True, screen_clear=True, slowtype=True, long=True)

# input
def get_target(limit):
    # advanced function defined to return an integer only, will check for exit prompts
    while True:
        clear()
        print(" > Choose a number between < ")
        print(f'1 - {limit}')
        target = check_exit()
        target = try_for_int(target)
        if target:
            if (type(target) == type(6) and target > 0
            and target < limit):
                return target
        else:
            print_s(" you must choose a number Between the provided range ", protected=True, screen_clear=True, slowtype=True, long=True)

def check_exit(skip_line=False, back_out=False):
    """ replaces the input prompt to check for any exit words then passes input back """
    print_s(None, sleep_skip=True, head_lines=(1 if skip_line else 0))
    keywords = input(get_option("DEFAULT_CURSOR"))
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
        for numb, option in enumerate(get_option("TEST_SIZE"), 1):
            print_s(f"{numb}) {option}", protected=True, half_step=True, sleep_skip=True)
        choice = check_exit()
        if choice:
            choice = try_for_int(choice, index=True)
            if (type(choice) == type(5) and choice >= 0 
            and choice < len(get_option("TEST_SIZE"))):
                data_sample = []
                if not sorted:
                    for _ in range(get_option("TEST_SIZE")[choice]):
                        data_sample.append(randint(1, get_option("RANDOM_UPPER_LIMIT")))
                    return data_sample
                for n in range(get_option("TEST_SIZE")[choice]):
                    data_sample.append(n)
                return data_sample
            print_s("this input size is not accepted, try again from the list", protected=True, screen_clear=True, slowtype=True, long=True)
