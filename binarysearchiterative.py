def binary_search(input_array, value):
    """Your code goes here."""
    low = 0
    high = len(input_array)-1
    mid = 0
    
    while low<=high:
        mid = (low + high) / 2
        if value > input_array[mid]:
            low = mid + 1
        elif value < input_array[mid]:
            high = mid - 1
        else:
            return mid
    return -1
