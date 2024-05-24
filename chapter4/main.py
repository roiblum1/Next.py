def gen_secs():
    """
    Generator that yields seconds from 0 to 59.
    """
    for sec in range(60):
        yield sec

def gen_minutes():
    """
    Generator that yields minutes from 0 to 59.
    """
    for minute in range(60):
        yield minute
        
def gen_hours():
    """
    Generator that yields hours from 0 to 23.
    """
    for hour in range(24):
        yield hour

def gen_time():
    """
    Generator that yields time in the format HH:MM:SS for every second of a 24-hour period.
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)
                
def gen_years(start=2019):
    """
    Generator that yields years starting from the given start year.
    :param start: The year to start from (default is 2019).
    """
    while True:
        yield start
        start += 1
        
def gen_months():
    """
    Generator that yields months from 1 to 12.
    """
    for month in range(1, 13):
        yield month

def is_leap_year(year):
    """
    Determines if a given year is a leap year.
    :param year: The year to check.
    :return: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def gen_days(month, leap_year = True):
    """
    Generator that yields the days in a given month.
    :param month: The month for which to generate days (1-12).
    :param leap_year: Boolean indicating if it's a leap year (default is True).
    """
    num_of_days = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    for day in range(1, num_of_days.get(month, 0) + 1):
        yield day

def gen_date():
    """
    Generator that yields dates in the format YYYY/MM/DD HH:MM:SS starting from the year 2019 and continues indefinitely.
    """
    for year in gen_years():
        for month in gen_months():
            leap_year = is_leap_year(year)
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%04d/%02d/%02d %s" % (year, month, day, time)
                            
if __name__ == "__main__":
    count = 0
    for date in gen_date():
        count += 1
        if count % 1000000 == 0:
            print(date)