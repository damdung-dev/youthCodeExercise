from datetime import datetime, timedelta

def next_and_previous_day(day, month, year):
    date = datetime(year, month, day)
    next_day = date + timedelta(days=1)
    previous_day = date - timedelta(days=1)
    return next_day.strftime("%d/%m/%Y"), previous_day.strftime("%d/%m/%Y")

# Example usage
day, month, year = map(int, input("Enter day, month, year: ").split())
next_day, previous_day = next_and_previous_day(day, month, year)
print("Next day:", next_day)
print("Previous day:", previous_day)
