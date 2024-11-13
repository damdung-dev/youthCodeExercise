def duty_roster(year, start_weekday, month):
    # Days in each month
    days_in_month = [31, 29 if calendar.isleap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    people = ['A', 'B', 'C', 'D', 'E']
    
    print("Sun Mon Tue Wed Thu Fri Sat")
    # Print leading spaces for the first week
    print("    " * start_weekday, end="")
    
    # Print days with duty person assignment
    for day in range(1, days_in_month[month-1] + 1):
        if start_weekday % 7 == 0 and day > 1:
            print()  # New line at the start of each week
        duty_person = people[(day - 1) % 5] if start_weekday % 7 != 0 else " "
        print(f"{day:2} [{duty_person}]" if duty_person != " " else f"{day:2}   ", end=" ")
        start_weekday += 1

# Example usage
year = int(input("Enter the year: "))
start_weekday = int(input("Enter the starting weekday of the year (0=Sun, 6=Sat): "))
month = int(input("Enter the month (1-12): "))
duty_roster(year, start_weekday, month)
