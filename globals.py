from buble_sort import bubble_sort

OPTIONS = {
    "CLEAR_SPEED": 2,   # how fast the prompt stops before freshing, for longer holds use a input statement
    "INTEGRITY_SKIP": False,  # should only be used for debuging; test runs in o(N)
    "FULL_AUTO": False,  # full auto true will allow to skip all enter prompts so that ALL the algo's can run then log out to a SQL file
}

ALGORITHM_OPTIONS = [{
    "name": "Bubble Sort", 
    "function": bubble_sort
},]

SETTINGS_KEYWORDS = [
    "settings", "config", "options", "option", "setting", "configure",
]

EXIT_WORDS = [
    "quit", "exit", "end", "stop", "esc"
]

EXIT_MESSAGE = """ This is the exit message """
