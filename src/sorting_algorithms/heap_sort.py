def heapify(values, current_index, max_index):
    """
    Recursive function to heapify an iterable of values. Assumes the gt function is implemented for values in iterable.

    Values are assumed in a heap tree format where the left child index is calculated by `2 * current_index + 1`
    and the right child index is calculated by `2 * current_index + 2`.
    Child indices higher than the max_index are ignored.
    When the value at the child index is higher than the value at the current index, the values are swapped and the
    current function is called recursively to compare the next layer of children.

    :param values: Iterable with values that can be compared using gt function
    :param current_index: int, the index of the current value being looked at
    :param max_index: int, maximum index in the iterable of values to look at
    :return: Heapified iterable
    """
    left_child = 2 * current_index + 1
    right_child = 2 * current_index + 2
    largest_index = current_index

    if left_child < max_index and values[left_child] > values[largest_index]:
        largest_index = left_child

    if right_child < max_index and values[right_child] > values[largest_index]:
        largest_index = right_child

    if largest_index != current_index:
        tmp = values[current_index]
        values[current_index] = values[largest_index]
        values[largest_index] = tmp

        values = heapify(values, largest_index, max_index)

    return values


def build_heap(values):
    """
    Builds a valid heap (where every root node's value is higher than or equal to it's children)
    Starts in to the middle of the iterable (`round(n / 2) - 1`) and works back to index 0

    :param values: Iterable with values that can be compared using gt function
    :return: Iterable values as valid heap
    """
    n = len(values)
    for i in range((round(n / 2) - 1), -1, -1):
        values = heapify(values, i, n)
    return values


def heap_sort(values):
    """
    Sort an iterable with values using a heap.
    The original values iterable is first heapified, then a loop is started that works its way back
    from index `len(values) - 1` to index 1* by creating a subarray up to that point and heapifying the subarray.
    Then the highest value in the heapified subarray (heap[0]) is swapped with the highest index of the subarray.

    *Note that a subarray for index 0 has a length of one and so does not need to be heapified nor swapped.

    :param values: Iterable with values that can be compared using gt function
    :return: Iterable with sorted values
    """
    values = build_heap(values)
    for i in range(len(values) - 1, 0, -1):
        tmp = values[0]
        values[0] = values[i]
        values[i] = tmp
        values = heapify(values, 0, i)
    return values


if __name__ == '__main__':
    assert heap_sort([3, 4, 2, 7, 1]) == [1, 2, 3, 4, 7]
    assert heap_sort([3, 4, 2, 7, 1, 2]) == [1, 2, 2, 3, 4, 7]
    assert heap_sort([1, 2, 3, 4, 7]) == [1, 2, 3, 4, 7]
