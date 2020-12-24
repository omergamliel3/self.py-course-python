def shift_left(my_list=[]):
    """
    shift all my_list object to the left
    :param my_list: the list argument
    :type my_list: list
    :rtype: list
    """

    # if list length is not 3 stop the function
    if len(my_list) != 3:
        return
    # store my list object is a, b, c
    a, b, c = my_list
    # create new list with shifted object
    shifted_list = [b, c, a]
    # return shifted_list
    return shifted_list


def shift_left_complex(my_list=[]):
    """
      shift all my_list object to the left
      :param my_list: the list argument
      :type my_list: list
      :rtype: list
    """

    if len(my_list) < 2:
        return

    shifted_list = []

    first_value = my_list[0]

    for x in my_list:
        if not x == first_value:
            shifted_list.append(x)

    shifted_list.append(first_value)

    return shifted_list


def main():
    # call function shift left
    # print('\n', shift_left(['monkey', 2.0, 1]))
    print('\n', shift_left_complex([1, 2, 3, 4]))


if __name__ == '__main__':
    main()
