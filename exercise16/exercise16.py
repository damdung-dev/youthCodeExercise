def zeller_formula(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    K = year % 100
    J = year // 100
    f = day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)
    return f % 7

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def print_calendar(year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29

    for month in range(1, 13):
        print(f"Tháng {month}")
        print("S  M  T  W  T  F  S")
        start_day = zeller_formula(year, month, 1)
        print("   " * start_day, end="")

        for day in range(1, days_in_month[month-1] + 1):
            print(f"{day:2d} ", end="")
            if (start_day + day) % 7 == 0:
                print()
        print("\n")
    print(f"ngày đầu tiên của năm là thứ: {zeller_formula(year, month, day)}")
year=int(input("nhập vào năm: "))
print_calendar(year)