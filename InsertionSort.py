import random


def comparison_function(array_value, key):
    if array_value >= key:
        return True
    else:
        return False


def insert_sort_array(array: list):
    """
    Sorts the given array in an order as according to the comparison_function.

    Parameters:
    array (list): The list to be sorted.

    Returns:
    list: The sorted list.

    Algorithm:
    1. Iterate through the keys in the array.
    2. For each key, compare it with all the previous keys and insert it into the correct position.
    3. If the key is already in the correct position, move on to the next key.
    4. If the key is smaller than the previous keys, shift the previous keys to the right and insert the key in the correct position.
    5. Repeat steps 2-4 until all keys have been processed.
    6. Return the sorted array.
    """
    array_length = len(array) - 1
    if array_length == 0 or array_length == 1:
        return array

    ### Iterate Throught the Keys
    for index in range(1, array_length):
        key = array[index]
        ##### For each key we need to look through all the previous keys
        for inner_index in range(0, index):

            ref_index = index - inner_index - 1

            ### If the key is in the right spot we insert it into this location
            if comparison_function(array[ref_index], key):
                array.pop(index)
                array.insert(ref_index + 1, key)
                break
            ### If this is the last loop then we need to store it at the beginning
            elif ref_index == 0:
                array.pop(index)
                array.insert(0, key)

            ### Else We Loop
    return array


array = [random.randint(0, 100) for i in range(10)]
print(array)
array = insert_sort_array(array)
print(array)
