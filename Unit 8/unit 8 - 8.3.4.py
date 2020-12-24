def inverse_dict(my_dict={}):
    """
    inverse a dict, keys -> values, values -> keys
    :param my_dict: dict argument to inverse
    :type my_dict: dict
    :rtype: dict
    """
    in_dict = {}
    for key, value in my_dict.items():
        in_dict[value] = in_dict.get(value, [])
        in_dict[value].append(key)
    return in_dict


def main():
    # call inverse dict func
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))


if __name__ == '__main__':
    main()