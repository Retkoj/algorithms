"""
Implementations of a multiplication function, Adapted from Java code in:
Algorithms in a Nutshell (G. T. Heineman, G. Pollice, S. Selkow), 2nd Edition, 2016, chapter 2
"""


def multiply(n1: list, n2: list):
    """
    Multiplication function in which the individual numbers of the lhs and rhs are stored in a list and the output
    number is also stored in a list

    :param n1: list, left hand side. e.g. [1, 2, 3]
    :param n2: list, right hand side. e.g. [4, 5, 6]
    :return: list, result of multiplying n1 and n2. Initialized to a list of zeros of length `max(len(n1), len(n2)) * 2`
        e.g. [0, 5, 6, 0, 8, 8]
    """
    max_outcome_length = max(len(n1), len(n2)) * 2
    result = [0] * max_outcome_length
    position = max_outcome_length - 1

    for i in range((len(n1) - 1), -1, -1):
        off = len(n1) - 1 - i
        for j in range((len(n2) - 1), -1, -1):
            product = n1[i] * n2[j]

            result[position - off] += product % 10
            result[position - off - 1] += result[position - off] // 10 + product // 10
            result[position - off] %= 10

            off += 1
    return result


if __name__ == '__main__':
    print("Testing 'multiply' function")
    print("Asserting: [1, 2, 3] * [4, 5, 6] = [0, 5, 6, 0, 8, 8]")
    assert multiply([1, 2, 3], [4, 5, 6]) == [0, 5, 6, 0, 8, 8], f"Expected [0, 5, 6, 0, 8, 8], " \
                                                                 f"but got {multiply([1, 2, 3], [4, 5, 6])}"

    print("Asserting: [4] * [7] = [2, 8]")
    assert multiply([4], [7]) == [2, 8], f"Expected [2, 8], but got {multiply([4], [7])}"
