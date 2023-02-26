# Test file for all things linear

import test_loader

# main variables
test_data = test_loader.get_input_size()
integrity_skip = False
time_taken = 0

# integrity test skip
""" should only be used for testing that may take an exessive amount of time 
the integrity test would double the time the testing can take to finish which can be problematic on longer tests 
like: O(!) then linear searching 100,000 bits!!"""
integrity_skip=False
if integrity_skip:
    passed_integrity = True

# get current time before running
for firstIterator in test_data:
    for secondIterator in test_data:
        if firstIterator > secondIterator:
            swapVar = secondIterator
            secondIterator = firstIterator
            firstIterator = swapVar

# get time after running
# get difference on times and store this number

#test the integrity of the sort using a linear search

# print how long it took and note wheather or note the integrity test passed


# closure or loopback
