def insertion_sort(values):
    """
    Sorts an Iterable of values by checking whether the previous value is higher than the current value. Requires
    a gt function to be implemented for values in the Iterable.
    If so, the previous value is moved to the current value's location.
    Moves through the list left to right, starting at index 1, and for every value checks (and -if needed- moves)
    all previous values.
    After moving the higher values one step to the right, the current value is inserted before those values.

    Example:
    l = [3, 2, 1]

    round 1:
    index = 1, current value = 2
    3 is higher than 2
    3 is moved to index 1
    No more previous values: 2 is inserted in index 0
    output round 1: [2, 3, 1]

    round 2:
    index = 2, current value = 1
    3 is higher than 1
    3 is moved to index 2
    2 is higher than 1
    2 is moved to index 1
    No more previous values: 1 is inserted in index 0
    output round 2: [1, 2, 3]

    :param values: Iterable with values to be sorted. Expected to have a lt/gt functionality implemented
    :return: Sorted Iterable with values
    """
    for i in range(1, len(values)):
        j = i - 1
        current_value = values[i]
        while j >= 0 and values[j] > current_value:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = current_value
    return values


if __name__ == '__main__':
    assert insertion_sort([3, 4, 2, 7, 1]) == [1, 2, 3, 4, 7]
