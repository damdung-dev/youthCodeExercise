import numpy as np

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(day, month, year):
    days_in_month = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    if is_leap_year(year):
        days_in_month[1] = 29
    return np.sum(days_in_month[:month-1]) + day
    
day=int(input("nhap vao ngay: "))
month=int(input("nhap vao thang: "))
year=int(input("nhap vao nam: "))
is_leap_year(year)
print("ngày thứ: " + str(day_of_year(day, month, year)))

