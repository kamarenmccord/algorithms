# Test file for all things linear
import test_loader
from buble_sort import bubble_sort

# main variables
test_data = test_loader.get_input_size()
integrity_skip = False
time_taken = 0
start_time = 0
end_time = 0

# integrity test skip
"""
should only be used for testing 
this may take an exessive amount of time 
the integrity test can double the time or worse 
like: O(!) then linear searching (test) 100,000 entities!!
"""
integrity_skip=False
if integrity_skip:
    passed_integrity = True

# get current time before running
start_time = test_loader.check_time()

# Do a sort - may be a function call later
bubble_sort(test_data)


# get time after running
end_time = test_loader.check_time()
# get difference on times and store this number
time_taken = end_time - start_time

#test the integrity of the sort
if not integrity_skip:
    test_passed = test_loader.integrity_check(test_data)
    print(f'Integrity test passed: {test_passed}')
    if test_passed == False:
        print(test_data[:25])

# print how long it took to sort
print(test_loader.time_calc(start_time, end_time, len(test_data)))
