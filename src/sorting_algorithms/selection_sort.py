def find_max_value_index(values, lower_index, upper_index):
    """
    Finds and returns the index of the maximum value in an Iterable, given the lower_index and upper_index bounds

    :return: int, index of maximum value within values[lower_index, upper_index]
    """
    max_index = lower_index
    for i in range(lower_index + 1, upper_index + 1):
        if values[i] > values[max_index]:
            max_index = i
    return max_index


def selection_sort(values):
    """
    Sorts the values in an Iterable with an implemented gt function by finding the index of the maximum value
    in the iterable and moving that value to the last index of the iterable. In the next round, the last index is not
    considered, and the next maximum value is moved to the second to last index, etc.

    :return:Sorted values
    """
    for i in range(len(values) - 1, -1, -1):
        max_index = find_max_value_index(values, 0, i)
        if max_index != i:
            tmp = values[i]
            values[i] = values[max_index]
            values[max_index] = tmp
    return values


if __name__ == '__main__':
    assert selection_sort([3, 2, 1]) == [1, 2, 3]
    assert selection_sort([1, 2, 3]) == [1, 2, 3]
