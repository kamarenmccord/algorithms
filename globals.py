"""
Holds the global settings and variables and 
other various important data that we need access 
to everywhere
~ like a global layer/scope of data
"""

from buble_sort import bubble_sort
from binary_search import binary_search

OPTIONS = {
    "CLEAR_SPEED": 2,   # how fast the prompt stops before freshing, for longer holds use a input statement
    "INTEGRITY_SKIP": False,  # should only be used for debuging; test runs in o(N)
    "FULL_AUTO": False,  # full auto true will allow to skip all enter prompts so that ALL the algo's can run then log out to a SQL file
    "TEST_SIZE" : [10**2*2, 10**3, 10**4*5, 10**5],
    "RANDOM_UPPPER_LIMIT": 10000,  # random number generation will happen between 1 and this number
}

# fixed options wont show as adjustable, these should only be affected by the application
FIXED_OPTIONS = ["FULL_AUTO", "TEST_SIZE"]

SETTINGS_KEYWORDS = [
    "settings", "config", "options", "option", "setting", "configure",
]

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

EXIT_MESSAGE = """ This is the exit message """
