data = ("self", "py", 1.543)
format_string = f"Hello {data[0] + '.' + data[1]} learner, you have only {(str(data[2])[:3])} units left before you " \
                f"master the course! "


def key_func(t):
    """
    return second value of t (the number value)
    """
    return t[1]


def sort_prices(list_of_tuples=[]):
    """
    return sorted list from list_of_tuples.
    sort key is key_func
    :param list_of_tuples: list of tuples argument (default=0)
    :type list_of_tuples: list
    :rtype: list
    """
    return sorted(list_of_tuples, key=key_func)


def multiple_tuple(tuple1, tuple2):
    """
    returns a tuple containing all the pairs that can be created from tuple1, tuple2 arguments.
    :param tuple1: first tuple argument
    :type tuple1: tuple
    :param tuple2: second tuple argument
    :type tuple2: tuple
    :rtype: tuple
    """
    combine_list = []
    for x in tuple1:
        for y in tuple2:
            if (x, y) not in combine_list:
                combine_list.append((x, y))
            if (y, x) not in combine_list:
                combine_list.append((y, x))

    return tuple(combine_list)


# products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
# print(sort_prices(products))

# first_tuple = (1, 2)
# second_tuple = (2, 2)
# print(multiple_tuple(first_tuple, second_tuple))

def contain_in_list(my_list=[], value=''):
    """
    return true or false whatever value in my list
    :param my_list: for loop list argument
    :type my_list: list
    :param value: value to check if contains in list objects
    :type value: str
    :rtype: bool
    """
    for list_item in my_list:
        if value in list_item:
            return True
    return False


def sort_anagrams(list_of_strings=[]):
    """
    sort anagrams from list_of_strings to lists of anagrams in a list.
    :param list_of_strings: string list argument (default = [])
    :type list_of_strings: list
    :return: sorted anagram list
    :rtype: list
    """
    anagrams_list = []
    for item1 in list_of_strings:
        # temp list to store current anagram list
        temp_list = []
        # evoid duplicates
        if contain_in_list(anagrams_list, item1):
            continue
        # loop over all values in list_of_strings
        for item2 in list_of_strings:
            # compare the letters with sorted
            if sorted(item1) == sorted(item2):
                # if item2 not in temp_list append the item
                if item2 not in temp_list:
                    temp_list.append(item2)

        # append temp list to anagrams_list
        anagrams_list.append(temp_list)

    return anagrams_list


def main():
    # call func sort anagrams
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                     'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))


if __name__ == '__main__':
    main()



