""" preforms binary search """

def binary_search(data_sample, target):
    """ 
    Data sample has to be already sorted
    target is what the program is looking for
    binary search splits the sample in half each time until the results are found
    """
    def recurse(arr, low, high, x):
        if high >= low:
            mid = (high + low)//2

            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return recurse(arr, low, mid-1, x)
            else:
                return recurse(arr, mid+1, high, x)

        else:
            return -1
    
    recurse(data_sample, 0, len(data_sample)-1, target)
    return True
