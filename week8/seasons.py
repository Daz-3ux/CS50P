from datetime import datetime
from datetime import date
import re
import sys
import inflect


def main():
    birth = get_birth()
    today = date.today()
    sub = date_sub(birth, str(today)).total_seconds() / 60
    minutes = convert_secondes(round(sub)).capitalize().replace("and ", "")
    print(f"{minutes} minutes")


def convert_secondes(sub):
    p = inflect.engine()
    words = p.number_to_words(sub)
    return words


def date_sub(birth, today):
    birth_matches = re.match(r"([1-9][0-9]{3})-([0-3][0-9])-([0-3][0-9])", birth)
    today_mathes = re.match(r"([1-9][0-9]{3})-([0-3][0-9])-([0-3][0-9])", today)
    datetime_birth = datetime(int(birth_matches.group(1)), int(birth_matches.group(2)), int(birth_matches.group(3)), 0, 0)
    datetime_today = datetime(int(today_mathes.group(1)), int(today_mathes.group(2)), int(today_mathes.group(3)), 0, 0)
    return datetime_today - datetime_birth

# Janury 1, 1999: False
# 1999-01-01: True
def get_birth():
    try:
        birth = input("Date of Birth: ")
        if matches := re.match(r"([1-9][0-9]{3})-([0-3][0-9])-([0-3][0-9])", birth):
            month = int(matches.group(2))
            day = int(matches.group(3))
            if(month < 1 or month > 12 or day < 1 or day > 31):
                raise ValueError
            return birth
        else:
            raise ValueError
    except ValueError:
        sys.exit("Invalid date")
    


if __name__ == "__main__":
    main()