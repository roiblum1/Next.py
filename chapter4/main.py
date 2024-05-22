def gen_secs():
    for sec in range(60):
        yield sec

def gen_minutes():
    for minute in range(60):
        yield minute
        
def gen_hours():
    for hour in range(24):
        yield hour

def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)
                
def gen_years(start=2019):
    while True:
        yield start
        start += 1
        
def gen_months():
    for month in range(1, 13):
        yield month

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def gen_days(month, leap_year = True):
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