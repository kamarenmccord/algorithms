
def bubble_sort(test_data):
    # Bubble sort O(N^2)
    length = len(test_data)
    for i in range(length):
        already_sorted = True
        for j in range(length-i-1):
            if test_data[j] > test_data[j+1]:
                test_data[j], test_data[j+1] = test_data[j+1], test_data[j]
                already_sorted = False
        if already_sorted:
            break