def print_dummy_text():
    """
    print dummy_text file
    """
    with open(r"text_files/dummy_text.txt", 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            print(line)


def are_files_equal(file1, file2):
    """
    return true if files text are equal, false if not.
    :param file1: first file path
    :type file1: file
    :param file2: second file path
    :type file2: file
    :rtype: bool
    """
    with open(file1, "r") as input_file:
        text1 = input_file.read()
    with open(file2, "r") as input_file:
        text2 = input_file.read()
    return text1 == text2

def main():
    # call are_files_equal
    print(are_files_equal('text_files/dummy_text.txt', 'text_files/some_text.txt'))


if __name__ == '__main__':
    main()