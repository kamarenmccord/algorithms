"""
Holds the global settings and variables and 
other various important data that we need access 
to everywhere
~ like a global layer/scope of data
"""
from colorama import Fore
from buble_sort import bubble_sort
from binary_search import binary_search

OPTIONS = {
"CLEAR_SPEED": {
    "OPTION": 2,
    "MINIMUM": 1,
    "MAXIMUM": 5,
    "MESSAGE": "How fast the prompt pauses before refreshing, number is in seconds \nrecommended range: 2-3",
    "SWITCHABLE": True
},"INTEGRITY_SKIP": {
    "OPTION": False,
    "MESSAGE": "Only for debugging, runs a test in O(N) will add exess time and can hider performance\nrecommended value: False",
    "SWITCHABLE": True
}, "RANDOM_UPPER_LIMIT": {
    "OPTION": 10000,
    "MINIMUM": 100,
    "MAXIMUM": 10**100,
    "MESSAGE": "upper bound limit that the random number generator will use, \nrecommended range: above 1000",
    "SWITCHABLE": True
}, "FULL_AUTO": {
    "OPTION": False,
    "MESSAGE":  "full auto true will allow to skip all enter prompts so that ALL the algo's can run then log out to a SQL file\nrecommended value: False",
    "SWITCHABLE": False
}, "TEST_SIZE": {
    "OPTION": [10**2*2, 10**3, 10**4*5, 10**5],
    "MESSAGE": "",
    "SWITCHABLE": False
}, "SKIP_DIALOGUE":{
    "OPTION": False,
    "MESSAGE": "Skip user freindly messages and data shows\nDefault False",
    "SWITCHABLE": True,
}, "DEFAULT_CURSOR": {
    "OPTION": "> ",
    "MINIMUM": 1,
    "MAXIMUM": 10,
    "MESSAGE" : "The default text input style\nrange:\n1 mimimum character\n 10 characters max",
    "SWITCHABLE": True,
}, "TEXT_COLOR":{
    "OPTION": Fore.WHITE,
    "SET": {"GREEN": Fore.GREEN, "BLUE": Fore.BLUE, "YELLOW": Fore.YELLOW, "BLUE": Fore.BLUE, "CYAN": Fore.CYAN, "WHITE": Fore.WHITE},
    "WARNING_COLOR": Fore.RED,
    "MESSAGE": "Changes the text color in the terminal",
    "SWITCHABLE": True,
}}

"""
Just import your function from the file and give the algorithm the options listed here!
@name : - the displayed name of the search / sort
@function: the imported function name
@search: True for search, False for sort
@message: if there is a message/warning list it here
"""
ALGORITHM_OPTIONS = [{
    "name": "Bubble Sort", 
    "function": bubble_sort,
    "search" : False,
    "warning": "The 2 largest data sets may take some time to sort",
},
{
    "name": "Binary Search",
    "function": binary_search,
    'search': True,
    "warning": False,
},]

EXIT_WORDS = [
    "quit", "exit", "end", "stop", "esc"
]

HELP_KEYWORDS = ["help", "h"]

SETTINGS_KEYWORDS = ["settings", "config", "options", "option", "setting", "configure", "s", "o"]

HELP_MESSAGE = """ 
Name
\tALGORITHM RUNNER

DESCRIPTION
\t source: https://github.com/kamarenmccord/algorithms
\t A CLI interface that allows you to run various algorithms

USEAGE
\t help - shows this interface
\t settings - opens the settings
\t quit - quits the program
\t Number - runs the specified algorithm
"""

EXIT_MESSAGE = """ Thanks for trying out my App\n I hoped this helped brought value to you\n\nhave a Great Day!! """

INTRO_MESSAGE = f"""
Welcome to the algorithm runner
This Program can execute many searches with various input sizes.
To see how long a search or sort will take choose one from a list and let it run!

      ฅ/ᐠ. ̫ .ᐟ\ฅ < Meow
{"==="*20}

press enter to continue...
"""
