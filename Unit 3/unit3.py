# print('\"Shuffle, Shuffle, Shuffle\", say it together! Change colors and \ndirections, Don\'t back down and stop
# the player! \n\t\tDo you want to play Taki? \n\t\tPress y\\n')


# encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
# print(encrypted_message[::-2])
# ''' one 'e' not at the end, two 'p' '''
# word = 'spaceship'

REPLACE_CHAR = 'e'
str = input('\nEnter a string: \t')
first_char = str[0]
print()
print(str[0] + str[1:].replace(first_char, REPLACE_CHAR))


