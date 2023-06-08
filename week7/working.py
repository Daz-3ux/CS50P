import re
import sys


def main():
    print(convert(input("Hours: ")))

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9 AM to 5:30
def convert(s):
    try:
        if matches := re.search(r"^(.+ (?:AM|PM)) to (.+ (?:PM|AM))$", s):
            begin_time, end_time = matches.group(1), matches.group(2)
            begin_time = format_time(begin_time)
            end_time = format_time(end_time)
            if check_time(begin_time) and check_time(end_time):
                begin_time = real_convert(begin_time)
                end_time = real_convert(end_time)
                return f"{begin_time} to {end_time}"
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        raise

def format_time(time):
    date, flag = time.split(" ")
    if date.find(":") != -1:
        begin, end = map(int, date.split(":"))
        if flag == "PM" and begin == 12:
            begin = 12
        elif flag == "AM" and begin == 12:
            begin = 0
        elif flag == "PM":
            begin += 12
        return f"{begin}:{end}"
    else:
        date = int(date)
        if flag == "PM" and date == 12:
            date = 12
        elif flag == "AM" and date == 12:
            date = 0
        elif flag == "PM":
            date += 12
        return str(date)


def check_time(time):
    if time.find(":") != -1:
        begin, end = map(int, time.split(":"))
        if(begin < 0 or begin > 24 or end < 0 or end > 59):
            return False
    else:
        if(int(time) < 0 or int(time) > 24 ):
            return False
    return True

def real_convert(time):
    if time.find(":") != -1:
        hour, minute = time.split(":")
        return f"{int(hour):02d}:{int(minute):02d}"
    else:
        return f"{int(time):02d}:00"

if __name__ == "__main__":
    main()