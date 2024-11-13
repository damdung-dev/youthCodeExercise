def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def duty_schedule(year, first_day, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29
    
    names = ['A', 'B', 'C', 'D', 'E']
    days = days_in_month[month - 1]
    
    print("Sun  Mon  Tue  Wen  Thu  Fri  Sat")
    for day in range(1, days + 1):
        if day == 1:
            print(" " * (first_day * 6), end="")
        if (first_day + day - 1) % 7 == 0:
            print()
        if (first_day + day - 1) % 7 != 0:
            print(f"{day:2d} [{names[(day - 1) % 5]}] ", end="")
        else:
            print(f"{day:2d} [ ]", end="")
year=int(input("năm: "))
first_day=int(input("thứ cho ngày đầu năm"))
month=int(input("tháng trong năm: "))
duty_schedule(year,first_day,month)