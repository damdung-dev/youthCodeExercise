def convert_hours(hours):
    weeks = hours // (7 * 24)
    days = (hours % (7 * 24)) // 24
    remaining_hours = hours % 24
    return weeks, days, remaining_hours

# Example usage
hours = int(input("Enter the number of hours: "))
weeks, days, remaining_hours = convert_hours(hours)
print(f"{weeks} week(s), {days} day(s), {remaining_hours} hour(s)")
