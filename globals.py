"""
Holds the global settings and variables and 
other various important data that we need access 
to everywhere
~ like a global layer/scope of data
"""

from buble_sort import bubble_sort

OPTIONS = {
    "CLEAR_SPEED": 2,   # how fast the prompt stops before freshing, for longer holds use a input statement
    "INTEGRITY_SKIP": False,  # should only be used for debuging; test runs in o(N)
    "FULL_AUTO": False,  # full auto true will allow to skip all enter prompts so that ALL the algo's can run then log out to a SQL file
    "TEST_SIZE" : [2000, 10000, 50000, 100000]
}

# fixed options wont show as adjustable, these should only be affected by the application
FIXED_OPTIONS = ["FULL_AUTO", "FULL_AUTO"]

SETTINGS_KEYWORDS = [
    "settings", "config", "options", "option", "setting", "configure",
]

"""
Just import your function from the file and give the algorithm the options listed here!
@name : - the displayed name of the search / sort
@function: the imported function name
@target: for searches to tell the app there will be a target to search for instead of sorting
@message: if there is a message/warning list it here
"""
ALGORITHM_OPTIONS = [{
    "name": "Bubble Sort", 
    "function": bubble_sort,
    "Target" : False,
    "warning": "The 2 largest data sets may take some time to sort",
},
{
    "name": "Binary Search",
    "function": bubble_sort,
    'target': True,
    "warning": False,
},]

EXIT_WORDS = [
    "quit", "exit", "end", "stop", "esc"
]

EXIT_MESSAGE = """ This is the exit message """
