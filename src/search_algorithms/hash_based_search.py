def hash_code(element, n_bins=13):
    """
    Converts  a string element into a hash value by converting every character to its ascii value, summing all values
    together iteratively while multiplying by 31 in every iteration.
    Converted from the hashCode function here:
    https://github.com/heineman/algorithms-nutshell-2ed/blob/17bd6e9cf9917727501f9eeadbfb2100f94eede0/Figures/src/algs/chapter5/example5/SimpleString.java

    :param element: str, item to be hashed
    :param n_bins: int, Number of hash bins
    :return: int, the absolute hash value modulo the number of bins
    """
    hashed_value = 0
    for char in element:
        hashed_value = 31 * hashed_value + ord(char)

    return abs(hashed_value) % n_bins


def create_hash_table(collection, hash_function):
    """
    Converts a collection of elements to a hash table using the hash_function, where elements from the collection
    are stored under their hash value. A single hash value can contain multiple elements.

    :param collection: Iterable, list with elements of a type that can be hashed by the hash_function
    :param hash_function: Function, calculates and returns the hash value for a given element
    :return: dict, dictionary with hash values as keys and collection items listed as values
    """
    table = {}
    for element in collection:
        hash_value = hash_function(element)
        if hash_value not in table.keys():
            table[hash_value] = [element]
        else:
            table[hash_value].append(element)
    return table


def hash_search(hash_table, target, hash_function):
    """
    Searches a hash_table for the target value by converting the target value to it's hash value, calculated by
    the hash_function, and looking it up in the hash_table. Returns whether the target is present in the hash table

    :param hash_table: dict, dictionary with hash values as keys and collection items listed as values
    :param target: target value, the type should be hashable by the hash_function
    :param hash_function: function, takes a value as input and returns the hash value
    :return: bool, Whether the target is found
    """
    target_found = False
    hash_value = hash_function(target)
    if hash_value in hash_table.keys():
        if target in hash_table[hash_value]:
            target_found = True
    return target_found


if __name__ == '__main__':
    list_of_words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    hash_table = create_hash_table(list_of_words, hash_code)
    assert hash_search(hash_table, 'fox', hash_code)
    assert not hash_search(hash_table, 'alphabet', hash_code)
