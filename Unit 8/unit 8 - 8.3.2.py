def info_dict():
    info = {'first_name': 'Mariah', 'last_name': 'Carey', 'birth_day': '27.03.1970', 'hobbies': 'Sing,Composer,Act'}
    while True:
        try:
            num = int(input('\nEnter a num between 1 to 8: (0 to quit program)\t'))
            if num == 0:
                quit()
            elif num == 1:
                print(info['last_name'])
            elif num == 2:
                print(info['birth_day'])
            elif num == 3:
                print('{} has {} hobbies'.format(info['first_name'], len(info['hobbies'].split(','))))
            elif num == 4:
                print('last hobie of {} is {}'.format(info['first_name'], info['hobbies'].split(',')[-1]))
            elif num == 5:
                info['hobbies'] = 'Sing,Composer,Act,Cooking'
            elif num == 6:
                birth_day_tuple = tuple(info['birth_day'].split('.'))
                print(birth_day_tuple)
            elif num == 7:
                age = int(input('%s, enter your age:\t' % info['first_name']))
                info['age'] = age
                print('Your age: %s' % info['age'])
            elif num == 8:
                for item in info.items():
                    print('%s -> %s' % item)
            else:
                print('\nYou can enter only digits between 1 and 8')
                assert ValueError
        except ValueError:
            print('\nYou can enter only digits between 1 and 8')


def count_chars(my_str):
    """
    the function takes string argument and return a dict so each element key is a char,
    and each element value is the number of times the char appears in the string argument
    :param my_str: string argument
    :type my_str: str
    :rtype: dict
    """
    my_dict = {}
    for letter in my_str:
        # evoid count space, and duplicate
        if letter.isalpha() and letter not in my_dict.keys():
            # count letter in my_str
            count_num = my_str.count(letter)
            # add key(letter), value(count_num) to my_dict
            my_dict[letter] = count_num

    return my_dict


magic_str = "abra cadabra"
for item in count_chars(magic_str).items():
    print('%s -> %s' % item)


