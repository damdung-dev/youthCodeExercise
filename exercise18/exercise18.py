def convert_hours(hours):
    weeks = hours // (24 * 7)
    days = (hours % (24 * 7)) // 24
    remaining_hours = hours % 24
    return weeks, days, remaining_hours

hours = 1000
weeks, days, hours = convert_hours(hours)
hour=int(input("enter the number of hours: "))
print(f"weeks={weeks} days={days} hours={hours}")