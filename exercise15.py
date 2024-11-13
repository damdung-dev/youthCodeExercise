from datetime import datetime

def day_of_year(day, month, year):
    date = datetime(year, month, day)
    start_of_year = datetime(year, 1, 1)
    day_number = (date - start_of_year).days + 1
    return day_number

# Example usage
day, month, year = map(int, input("Enter day, month, year: ").split())
print("Day of the year:", day_of_year(day, month, year))

