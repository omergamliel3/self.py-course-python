def copy_file_content(source, destination):
    """
    copy source text to destination.
    :param source: file path to copy
    :type source: str
    :param destination: file path to paste
    :type destination: str
    """
    try:
        with open(r"%s" % source, "r") as source_input:
            source_text = source_input.read()
    except FileNotFoundError:
        print('File Not Found')
    except:
        print('Error')
    try:
        with open(r"%s" % destination, 'w') as destination_input:
            destination_input.write(source_text)
    except FileNotFoundError:
        print('File Not Found')
    except:
        print('Error')


def who_is_missing(file_name):
    """
    The function takes a path parameter for a text file.
    The file's text contains a list of integers from 1 to n (not sorted, comma separated).
    One on the integers in the sequence is missing.
    The function returns the missing integer, and write it 'found.txt' file.
    :param file_name: file path
    :type file_name: str
    :return: the missing number in the sequence
    :rtype: int
    """
    missing_num = ''
    try:
        with open(r"%s" % file_name, "r") as file_name_input:
            file_text = file_name_input.read()
        sequence = sorted(file_text.split(','))
        for i in range(len(sequence)-1):
            if abs(int(sequence[i]) - int(sequence[i+1])) != 1:
                missing_num = str(int(sequence[i]) + 1)

    except FileNotFoundError:
        print('File Not Found')

    try:
        with open(r"text_files\found.txt", "w") as input_file:
            input_file.write(missing_num)
    except FileNotFoundError:
        print('File Not Found')

    return missing_num


def main1():
    # call func copy_file_content
    source_path = 'text_files\copy.txt'
    destination_path = 'text_files\paste.txt'
    copy_file_content(source_path, destination_path)


def main2():
    # call func who_is_missing
    missing_num = who_is_missing(r"text_files\find_me.txt")
    print('\nThe missing number is %s' % missing_num)


if __name__ == '__main__':
    main2()