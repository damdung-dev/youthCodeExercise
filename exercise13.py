def day_of_week(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    f = day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - 2 * j
    weekday = f % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[weekday]

# Example usage
day, month, year = map(int, input("Enter day, month, year: ").split())
print("Day of the week:", day_of_week(day, month, year))
