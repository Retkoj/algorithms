

def add(n1: list, n2: list):
    """
    Add function in which the left hand side and right hand side are assumed same length and the individual
    numbers are stored in a list

    :param n1: list, left hand side. e.g. [1, 2, 3]
    :param n2: list, right hand side. e.g. [4, 5, 6]
    :return: list, result of adding n1 and n2. Initialized to a list of zeros of length (len(n1) + 1). e.g. [0, 5, 7, 9]
    """
    position = len(n1) - 1
    result = [0] * (len(n1) + 1)
    carry = 0
    while position >= 0:
        total = n1[position] + n2[position] + carry
        result[position + 1] = total % 10
        carry = 1 if total > 9 else 0
        position -= 1
    result[0] = carry
    return result


if __name__ == '__main__':
    print("Asserting: [1, 2, 3] + [4, 5, 6] = [0, 5, 7, 9]")
    assert add([1, 2, 3], [4, 5, 6]) == [0, 5, 7, 9], f"Expected [0, 5, 7, 9], but got {add([1, 2, 3], [4, 5, 6])}"

    print("Asserting: [9, 9, 9] + [4, 5, 6] = [1, 4, 5, 5]")
    assert add([9, 9, 9], [4, 5, 6]) == [1, 4, 5, 5], f"Expected [0, 5, 7, 9], but got {add([1, 2, 3], [4, 5, 6])}"

