# unit 1 - python course

blocks_num = int(input('\nEnter three digits: '))
num1 = int(blocks_num / 100)
num2 = int((blocks_num / 10) % 10)
num3 = blocks_num % 10
combined = num1 + num2 + num3
print('\n', num1, num2, num3)
print('\n', combined)
print('\n', int(combined / 3))
print('\n', combined % 3 == 0)
flag = True
while flag:
    try:
        num = int(input('\nEnter a num '))
        print('\nYour num is:', num)
        print('\nYour num squared', num ** 2)
        flag = False
    except ValueError:
        print('\nAn error has been accrued, pls enter a valid number')
        flag = True

