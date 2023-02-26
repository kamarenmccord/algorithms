# Test file for all things linear

import test_loader

test_data = test_loader.get_input_size()

for firstIterator in test_data:
    for secondIterator in test_data:
        if firstIterator > secondIterator:
            swapVar = secondIterator
            secondIterator = firstIterator
            firstIterator = swapVar

#test it

# print it
print(test_data)
# closure or loopback
