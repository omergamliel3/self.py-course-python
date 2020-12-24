# Python Course - unit 4
# 4.2.3

flag = True
while flag:
    temperature = input('\nInsert the temperature you would like to convert:\t').lower()
    if temperature.endswith('f'):
        degF = int(temperature[:-1])
        deg_convert_c = ((degF * 5) - 160) / 9
        print(f'Convert to C:\t{deg_convert_c}C')
        flag = False
    elif temperature.endswith('c'):
        degC = int(temperature[:-1])
        deg_convert_f = ((degC * 9) + 32 * 5) / 5
        print(f'Convert to F:\t{deg_convert_f}F')
        flag = False
    else:
        print('string must end with f or c')
