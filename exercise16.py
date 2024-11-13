import calendar

def print_year_calendar(year):
    for month in range(1, 13):
        print(calendar.month(year, month))

# Example usage
year = int(input("Enter a year: "))
print_year_calendar(year)
