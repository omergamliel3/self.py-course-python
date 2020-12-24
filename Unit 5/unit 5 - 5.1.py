def last_early(str):
    """ last early function, return true if last char showed before, false if not """
    str = str.lower()
    if len(str) > 1:
        last_char = str[-1]
        if str[:-1].find(last_char) == -1:
            return False
        else:
            return True
    else:
        return False


def distance(num1, num2, num3):
    """ distance function """
    if (abs(num2 - num1) == 1 or abs(num3 - num1) == 1) and ((abs(num2 - num3) > 2 and abs(num2 - num1) > 2) or (
            2 < abs(num3 - num2) and abs(num3 - num1) > 2)):
        return True
    else:
        return False


def filter_teens(a=13, b=13, c=13):
    """ filter teens function, return sum of all arguments with fix_age function applied """
    return fix_age(a) + fix_age(b) + fix_age(c)


def fix_age(age):
    """ fix age helper function, return 0 if age > 15 and age < 12 or age > 16 and age < 20 """
    if 12 < age < 15 or 16 < age < 20:
        return 0
    else:
        return age


def chocolate_maker(small, big, x):
    """ chocolate maker function, return true if x can fit small and big arguments """
    return(small + big * 5) >= x


