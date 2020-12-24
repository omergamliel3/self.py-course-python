def are_lists_equal(list1=[], list2=[]):
    """
    compare between two lists. return true if equal, false if not.
    :param list1: first argument compare
    :type list1: list
    :param list2: second argument compare
    :type list2: list
    :return: true if lists are equals, false if not
    :rtype: bool
    """
    return sorted(list1) == sorted(list2)


def longest(my_list):
    """
    return longest value of my_list
    :param my_list: list argument to check longest value
    :type my_list: list
    :return: longest value in my_list
    :rtype: str
    """
    # call max function, pass my_list as argument
    return max(my_list)


def main():
    # call func are_lists_equal
    print('\n', are_lists_equal([1, 2, 3], [3, 1, 2]))
    # call func longest
    print('\n', longest(['1', '22', '333']))


if __name__ == '__main__':
    main()
