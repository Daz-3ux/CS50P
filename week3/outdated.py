def main():
    month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    format_month(month)
    
def format_month(months):
    while True:
        try:
            Date = input("Date: ").strip()
            if Date.find(",") != -1:
                Date = Date.split(",")
                month = Date[0].split(" ")[0]
                day = Date[0].split(" ")[1]
                year = Date[1].lstrip()
                if month in months:
                    month = months.index(month)+1
                format_date(month, day, year)
            elif Date.find("/") != -1:
                Date = Date.split("/")
                month = Date[0]
                day = Date[1]
                year = Date[2]
                format_date(month, day, year)
            else:
                continue
        except EOFError:
            exit()
        except ValueError:
            continue

def format_date(month, day, year):
    month = int(month)
    day = int(day)
    if day <= 0 or day > 31:
        pass
    elif month <= 0 or month > 12:
        pass
    else:
        print(f"{year}-{int(month):02d}-{int(day):02d}")
        exit()

main()