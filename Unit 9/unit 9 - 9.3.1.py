def my_mp3_playlist(file_path):
    """
    read file_path text and extract (with known pattern)
    max length song, number of songs, artist with the most appears.
    :param file_path: file path to song playlist
    :type file_path: str
    :return: a tuple with three parameters: max_len_song, lines_len, most_appears_artist
    :rtype: tuple
    """

    with open(file_path, 'r') as input_file:
        # split text file to lines
        splitted_lines = input_file.read().split('\n')
    # lines length
    lines_len = len(splitted_lines)
    # return splitted_lines element with max length song
    max_len_song = max(splitted_lines, key=lambda e: convert_time(e.split(';')[2]))
    # max length song name
    max_len_song = max_len_song.split(';')[0]

    # calculate artists appears
    # create a dict. loop all artists in splitted_lines.
    # set a key (artist name), value (1) for each artist.
    # if artist already exists add 1 to the value.
    artist_dict = {}
    for line in splitted_lines:
        artist = line.split(';')[1]
        if artist_dict.get(artist, 0) == 0:
            artist_dict[artist] = 1
        else:
            artist_dict[artist] += 1

    # return key (artist) of max length value
    most_appears_artist = max(artist_dict, key=lambda key: artist_dict[key])
    # return tuple
    return max_len_song, lines_len, most_appears_artist


def convert_time(song_len=''):
    """
    convert song_len string format x:xx (5:13) to seconds (int).
    :param song_len: song length in x:xx format
    :type song_len: str
    :return: song length in seconds
    :rtype: int
    """
    # split song_len to min and seconds
    splitted_time = song_len.split(':')
    # multiple the minutes, add the remaining seconds
    return int(splitted_time[0] * 60) + int(splitted_time[1])


def my_mp4_playlist(file_path, new_song):
    """
    replace third line song name with new_song argument in file_path.
    print new file_path text.
    :param file_path: file path
    :type file_path: str
    :param new_song: song to replace
    :type new_song: str
    """
    with open(file_path, 'r') as input_file:
        # split text file to lines
        splitted_lines = input_file.read().split('\n')
        # split third line to song name, artist name, song length
        splitted_third_line = splitted_lines[2].split(';')
        # put new_song argument instead original song name
        new_element = [new_song] + splitted_third_line[1:]
        # assign new element to list in the third index
        splitted_lines[2] = ';'.join(new_element)

    with open(file_path, 'w+') as input_file:
        # update file_path with new text
        for line in splitted_lines:
            input_file.write("%s\n" % line)

    with open(file_path, 'r') as input_file:
        # print updated file_path
        print(input_file.read())


def main():
    # call func my_mp3_playlist
    file_path = r'text_files\playlist.txt'
    # print(my_mp3_playlist(file_path))
    # call func my_mp4_playlist
    my_mp4_playlist(file_path, 'Physical')


if __name__ == '__main__':
    main()

#    input_file.write("%s:%s\n" % (key, value))
