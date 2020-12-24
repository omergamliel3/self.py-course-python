# Python Course - unit 4
# 4.2.2

str = input('Enter a string:\t')
str = str.replace(' ', '').lower()
print(f'\n{str} : {str[::-1]}\n')
if str == str[::-1]:
    print('OK')
else:
    print('NOT')
