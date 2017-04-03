def is_leap_year(year):

    def is_divisible(num, val):
        return val % num == 0

    if is_divisible(4, year) and not is_divisible(100, year) or is_divisible(400, year):
        return True
    else:
        return False


print is_leap_year(2016)
