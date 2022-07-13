def binary_search(input_array, value):
    """Your code goes here."""
    num_of_elements = len(input_array)
    mid = int(num_of_elements/2)
    if num_of_elements == 1 and value != input_array[0]:
        return -1
    else:
        if value == input_array[mid]:
            return input_array[mid]
        elif value > input_array[mid]:  
            return binary_search(input_array[mid+1:],value)
        elif value < input_array[mid]:
            return binary_search(input_array[:mid], value)
        else:
          return -1
