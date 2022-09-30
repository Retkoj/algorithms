def binary_search(sorted_collection, target):
    """
    requires a sorted collection where C[i] < C[j] is true if i < j and where the target is comparable to the elements
    in the collection using a gt/lt function.

    Searches for the target in the sorted collection using the following steps:

    1. Set the lower and upper index, starting with 0 to n - 1
    2. Retrieve the middle index in the index range (lower + upper) // 2
    3. Compare the value at the middle index with target
      - If the target is higher, set the middle index + 1 as the lower bound and go to step 2
      - If the target is lower, set the middle index as the upper index and go to step 2
      - If the target is equal, return True

    If the target is not found, False is returned

    :param sorted_collection: Iterable, Collection of sorted elements
    :param target: Same type as the elements in the collection
    :return: Boolean, Whether the target exists in the sorted_collection
    """
    lower_bound = 0
    upper_bound = len(sorted_collection)
    while lower_bound < upper_bound:
        middle_index = (upper_bound + lower_bound) // 2
        if sorted_collection[middle_index] < target:
            lower_bound = middle_index + 1
        elif sorted_collection[middle_index] > target:
            upper_bound = middle_index
        elif sorted_collection[middle_index] == target:
            return True
    return False


if __name__ == '__main__':
    assert binary_search([1, 2, 3, 4, 7], 1)
    assert binary_search([1, 2, 3, 4, 7], 2)
    assert binary_search([1, 2, 3, 4, 7], 3)
    assert binary_search([1, 2, 3, 4, 7], 4)
    assert binary_search([1, 2, 3, 4, 7], 7)
    assert not binary_search([1, 2, 3, 4, 7], 8)
    assert not binary_search([1, 2, 3, 4, 7], -1)
