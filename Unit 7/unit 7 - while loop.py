def squared_numbers(start=0, stop=0):
    """
    return a list with squared nums between start and stop
    :param start: start num argument (default = 0)
    :type start: int
    :param stop: stop num argument (default = 0)
    :type stop: int
    :rtype: list
    """
    # condition to continue
    if not start <= stop:
        return None

    # squared list to store squared nums
    squared_list = []
    # iterate from start to stop
    while start <= stop:
        # append stat squared to list
        squared_list.append(start ** 2)
        # add 1 to start
        start += 1
    # return squared list after appending all squared nums
    return squared_list


def is_greater(my_list=[], n=0):
    """
    return list with all numbers that greater then n argument
    :param my_list: list argument to check values from (default = [])
    :param n: int argument to check values if greater than (default = 0)
    :rtype: list
    """
    greater_list = []
    for item in my_list:
        if item > n:
            greater_list.append(item)
    return greater_list


def numbers_letters_count(my_str=''):
    """
    return list - first value represent num of digits of my_str,
    second value represent num of non digits chars of my_str
    :param my_str: str value
    :type my_str: str
    :rtype: list
    """
    r_list = [0, 0]
    for item in my_str:
        if item.isdigit():
            r_list[0] += 1
        else:
            r_list[1] += 1
    return r_list


def seven_boom(end_num=0):
    """
    simulate 'seven boom' game. return a list from 0 to end_num.
    replace 7 multiples and digits contains 7 with 'BOOM'
    :param end_num: end number argument (default = 0)
    :type end_num: int
    :rtype: list
    """
    seven_boom_list = []
    for num in range(0, end_num + 1):
        if num % 7 == 0 or '7' in str(num):
            seven_boom_list.append('BOOM')
        else:
            seven_boom_list.append(num)

    return seven_boom_list


def sequence_del(my_str=''):
    """
    return a list from my_str values with no duplicate letters
    :param my_str: str argument to del sequence
    :type my_str: str
    :rtype: list
    """
    my_list = list(dict.fromkeys(my_str))
    return my_list


def arrow(my_char='*', max_length=2):
    """
    return a graphical arrow shape str from my_char and max_length
    :param my_char: graphic char
    :param max_length: length of the arrow
    :rtype: str
    """
    if max_length < 2:
        return 'Failed'

    arrow_str = ''
    for num in range(1, max_length):
        arrow_str += my_char * num + '\n'
    for num in range(max_length, 0, -1):
        arrow_str += my_char * num + '\n'

    return arrow_str


def main():
    # call func squared_numbers
    # print('\n', squared_numbers(-3, 3))
    # call func is_greater
    # print('\n', is_greater([x for x in range(1, 11)], 5))
    # call func number_letters_count
    # print('\n', numbers_letters_count("Python 3.6.3"))
    # call func seven_boom
    # print('\n', seven_boom(17))
    # sequence_del('pprint')
    # print(arrow(max_length=10))
    pass


if __name__ == '__main__':
    main()
