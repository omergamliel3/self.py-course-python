def format_list(my_list=[]):
    """
    return a string of all the even index values and the last value of my_list
    :param my_list: the list argument
    :type my_list: list
    :rtype: string
    """

    # if my_list has no even length return ''
    if len(my_list) % 2 != 0:
        return ''

    # join , to all even list values, add 'and + {last value}'
    return ' ,'.join(my_list[::2]) + ' and ' + my_list[-1]


def extend_list_x(list_x, list_y):
    """
    extend list_y to list_x and return list_x
    :param list_x: first list argument
    :type list_x: list
    :param list_y: second list argument
    :type list_y: list
    :return: list_y + list_x as list
    :rtype: list
    """

    temp_list = list_x
    list_x = []
    for x in list_y:
        list_x.append(x)
    for x in temp_list:
        list_x.append(x)
    return list_x


def main():
    # call function format_list
    print('\n', extend_list_x([x for x in range(0, 10) if x % 2 == 0], [x for x in range(0, 10) if x % 2 == 1]))


if __name__ == '__main__':
    main()
