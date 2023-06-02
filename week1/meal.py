def main():
    time = input("What time is it? ").strip()
    converted_time = float(convert(time))
    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")

# 7:30 -> 7.5
# 7:30 a.m. -> 19.5
def convert(time):
    hour, left = time.split(":")
    if left.find(".m.") != -1:
      minute, flag = left.split(" ")
    else:
      minute = left
      flag = ""
    minute = str((float(minute) / 60)).split(".")[1]
    if flag == "p.m.":
      hour = str(int(hour) + 12)
    return hour + "." + str(minute)

if __name__ == "__main__":
    main()
