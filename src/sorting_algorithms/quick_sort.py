"""
Code adapted to Python from:
https://github.com/heineman/algorithms-nutshell-2ed/blob/master/JavaCode/src/algs/model/array/Selection.java
"""
from src.sorting_algorithms.insertion_sort import insertion_sort


def switch_values_at_indices(values, index_one, index_two):
    """
    Switches the values at index_one and index_two in place and returns the values iterable.
    """
    tmp = values[index_one]
    values[index_one] = values[index_two]
    values[index_two] = tmp
    return values


def partition(values, left, right, pivot_index):
    """
    Partition an iterable values by splitting on the value stored at pivot_index.
    Partitions so all values left of the pivot_value are le (<=) to the pivot value and all to the right are
    greater than the pivot value.
    The pivot value is stored at whatever index is between the partitions.

    :param values: Iterable with values that have gt/le functions implemented
    :param left: int, lowest index to look at
    :param right: int, highest index to look at
    :param pivot_index: int, index to start partition on (not necessarily the index of the median nor middle index)
    :return: Tuple, (Iterable with values reordered into partitions, store_index where the pivot_value ended up)
    """
    pivot_value = values[pivot_index]

    values = switch_values_at_indices(values, right, pivot_index)

    store_index = left
    for i in range(left, right):
        if values[i] <= pivot_value:
            values = switch_values_at_indices(values, i, store_index)
            store_index += 1

    values = switch_values_at_indices(values, right, store_index)
    return values, store_index


def select_pivot_index(values, left, right):
    """
    Selects a pivot index. Takes indices left (min), middle, right (max) and first compares the values at
    index left and middle. If the middle *value* is higher, then the *indices* of left and middle are swapped.
    Next comparisons are done to select the middle *value* of the values at the three indices. The index of the
    middle value is returned as a int.

    :param values: Iterable with values, gt/lt function should be implemented for values
    :param left: int, left bound index of (sub)array of values
    :param right: int, right bound index of (sub)array of values
    :return: int, chosen pivot index
    """
    middle_index = (left + right) // 2
    low_index = left

    if values[low_index] >= values[middle_index]:
        low_index = middle_index
        middle_index = left

    pivot_index = right
    if values[right] <= values[low_index]:
        pivot_index = low_index
    elif values[right] <= values[middle_index]:
        pivot_index = middle_index
    return pivot_index


def recursive_quick_sort(values, left, right, min_size_for_insertion=0):
    """
    Gets a pivot index, partitions the iterable values and either quick sorts or insertion sorts the partitions
    (depending on value set for min_size_for_insertion) in place.

    :param values: Iterable with values, should have gt/lt functions implemented for values
    :param left: int, left bound index of (sub)array of values
    :param right: int, right bound index of (sub)array of values
    :param min_size_for_insertion: int, If set to higher than 0, insertion sort will be used for partitions smaller than
        the size specified, to speed up the algorithm
    :return: Iterable with sorted values
    """
    if right <= left:
        return values

    pivot_index = select_pivot_index(values, left, right)
    values, pivot_index = partition(values, left, right, pivot_index)

    if pivot_index - 1 - left <= min_size_for_insertion:
        values[left: pivot_index] = insertion_sort(values[left:pivot_index])
    else:
        values = recursive_quick_sort(values, left, pivot_index - 1, min_size_for_insertion)

    if right - pivot_index - 1 <= min_size_for_insertion:
        values[pivot_index + 1: right + 1] = insertion_sort(values[pivot_index + 1: right + 1])
    else:
        values = recursive_quick_sort(values, pivot_index + 1, right, min_size_for_insertion)

    return values


def quick_sort(values, min_size_for_insertion=0):
    """
    Calls the recursive quick sort function, returns sorted values
    :param values: Iterable with values, should have gt/lt functions implemented for values
    :param min_size_for_insertion: int, If set to higher than 0, insertion sort will be used for partitions smaller than
        the size specified, to speed up the algorithm
    :return: Iterable with sorted values
    """
    return recursive_quick_sort(values, 0, len(values) - 1, min_size_for_insertion)


if __name__ == '__main__':
    assert quick_sort([3, 4, 2, 7, 1]) == [1, 2, 3, 4, 7]
    assert quick_sort([3, 4, 2, 7, 1, 2]) == [1, 2, 2, 3, 4, 7]
    assert quick_sort([1, 2, 3, 4, 7]) == [1, 2, 3, 4, 7]

    assert quick_sort([3, 4, 2, 7, 1], min_size_for_insertion=2) == [1, 2, 3, 4, 7]
    assert quick_sort([3, 4, 2, 7, 1, 2], min_size_for_insertion=2) == [1, 2, 2, 3, 4, 7]
    assert quick_sort([1, 2, 3, 4, 7], min_size_for_insertion=2) == [1, 2, 3, 4, 7]
