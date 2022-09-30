def sequential_search(collection, target):
    """
    Checks whether the target exists in the collection. If so, returns True, else returns False

    :param collection: Iterable, Collection of elements
    :param target: Same type as the elements in the collection
    :return: Boolean, Whether target is found
    """
    for element in collection:
        if element == target:
            return True
    return False


if __name__ == '__main__':
    assert sequential_search([3, 4, 2, 7, 1], 7)
    assert sequential_search(["Dog", "Cat", "Mouse"], "Dog")
    assert not sequential_search(["Dog", "Cat", "Mouse"], "Goat")
