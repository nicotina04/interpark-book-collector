import random as rd


month_day = {4: 30, 6: 30, 11: 30, 1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 9: 31, 10: 31, 12: 31}


def jsdate_to_clock(_date: str):
    ret = 0
    d, c = _date.split(' ')
    d = d.split('-')
    c = c.split(':')
    ret += int(d[0]) * 31284000
    ret += int(d[1]) * 2772000
    ret += int(d[2]) * 86400
    ret += int(c[0]) * 60 * 60
    ret += int(c[1]) * 60
    ret += int(c[2])
    return ret


def to_jsdate(s):
    ret = ''
    more = 0
    lt = s.split(' ')
    if lt[1] == "PM" and lt[2].split(':')[0] != '12':
        more = 12

    for i in range(len(lt[0])):
        if lt[0][i] == '/':
            ret += '-'
        else:
            ret += lt[0][i]

    clk = lt[2].split(':')
    ret += ' ' + str(int(clk[0]) + more) + ':' + clk[1] + ':' + clk[2]

    return ret


def add_head_zero(s: str):
    if len(s) == 1:
        return '0' + s
    else:
        return s


def get_days_from_month(year: int, month: int):
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return 29

    try:
        return month_day[month]
    except:
        return 0


def gen_date(start_year=2020, end_year=2020, start_month=1, end_month=12):
    year = rd.randrange(start_year, end_year + 1)
    month = rd.randrange(start_month, end_month + 1)
    day = rd.randrange(1, get_days_from_month(year, month) + 1)
    hour = rd.randrange(9, 20)
    minute = rd.randrange(1, 59)
    second = rd.randrange(1, 59)

    ret = str(year) + '-' + add_head_zero(str(month)) + '-' + add_head_zero(str(day)) + ' '
    ret += add_head_zero(str(hour)) + ':' + add_head_zero(str(minute)) + ':' + add_head_zero(str(second))

    return ret


if __name__ == '__main__':
    # Test method
    for _ in range(50):
        print(gen_date())
