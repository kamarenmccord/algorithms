"""File for the main meat of the application """
from os import system, name
from globals import EXIT_MESSAGE, EXIT_WORDS, ALGORITHM_OPTIONS


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
    pass

# input
def check_exit(skip_line=True):
    """ replaces the input prompt to check for any exit words then passes input back """
    if skip_line:
        print("\n")
    keywords = input("> ")
    if keywords.lower() in EXIT_WORDS:
        exit_function()
    return keywords
