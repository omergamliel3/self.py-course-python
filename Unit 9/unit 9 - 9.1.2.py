def file_program():
    while True:
        try:
            # take file path input
            file_path = input('\nEnter a file path:\t')
            if file_path == '':
                file_path = 'text_files\some_text.txt'
            # open file
            input_file = open(r"%s" % file_path, "r")
            # read file
            file_text = input_file.read()
            # separate file text to lines
            lines = file_text.split('\n')
            # take task input
            task = input('\nEnter a task:\t')
            if task == 'sort':
                join_text = ' '.join(lines)
                print(sorted(list(dict.fromkeys(join_text.split(' ')))))
                input_file.close()
                break
            elif task == 'rev':
                for line in lines:
                    print(''.join(line[::-1]))
                input_file.close()
                break
            elif task == 'last':
                line_num = int(input('\nEnter a num:\t')) - 1
                if line_num > len(lines):
                    print('\nNum must be small or equal to %d' % len(lines))
                    continue
                print()
                for line in lines[line_num:]:
                    print(''.join(line))
                input_file.close()
                break
            else:
                print('\nEnter a valid task')
                continue

        except FileNotFoundError:
            print('\nFile not found')
            continue
        except ValueError:
            print('\nAn error has been occurred')
            continue


def main():
    # call func file_program
    file_program()


if __name__ == '__main__':
    main()