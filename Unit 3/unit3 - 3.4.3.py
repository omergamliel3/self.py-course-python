str = input('Enter a string, at least 2 chars:\t')
str_half_length = len(str) // 2
print(str[:str_half_length].lower() + str[str_half_length:].upper())

