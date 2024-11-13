from functools import cache
@cache

def nextday(day, month,year):
    month_list30=[2,4,7,8,9,11]
    month_list31=[3,5,6,10]
    if year%4==0 and year%100!=0 or year%400==0:
        if month==2 and day==29:
            month+=1
            day=1
            print(f"next day: {day}/{month}/{year}")
        elif month in month_list30 and day==30:
            month+=1
            day=1
            print(f"next day: {day}/{month}/{year}")
        elif month in month_list31 and day==31:
            month+=1
            day=1
            print(f"next day: {day}/{month}/{year}")
        elif month==1 and day in range(2,32):
            day+=1
            print(f"next day: {day}/{month}/{year}")
        elif month==12 and day in range(1,31):
            day+=1
            print(f"next day: {day}/{month}/{year}")
        elif month==12 and day==31:
            month=1
            day=1
            year+=1
            print(f"next day: {day}/{month}/{year}")
        else:
            day+=1
            print(f"next day: {day}/{month}/{year}")
    else:
        if month==2 and day==28:
            month+=1
            day=1
            print(f"next day: {day}/{month}/{year}")
        elif month in month_list30 and day==30:
            month+=1
            day=1
            print(f"next day: {day}/{month}/{year}")
        elif month in month_list31 and day==31:
            month+=1
            day=1
            print(f"next day: {day}/{month}/{year}")
        elif month==12 and day==31:
            month=1
            day=1
            year+=1
            print(f"next day: {day}/{month}/{year}")
        elif month==1 and day in range(2,32):
            day+=1
            print(f"next day: {day}/{month}/{year}")
        elif month==12 and day in range(1,31):
            day+=1
            print(f"next day: {day}/{month}/{year}")
        else:
            day+=1
            print(f"next day: {day}/{month}/{year}")
        

def previousday(day,month,year):
    month_list30=[2,4,7,8,9,11]
    month_list31=[3,5,6,10]
    if year%4==0 and year%100!=0 or year%400==0:
        if month==3 and day==1:
            month=2
            day=29
            print(f"previous day: {day}/{month}/{year}")
        elif month in month_list30 and day==1:
            month-=1
            day=30
            print(f"previous day: {day}/{month}/{year}")
        elif month in month_list31 and day==1:
            month-=1
            day=31
            print(f"previous day: {day}/{month}/{year}")
        elif month==1 and day==1:
            month=12
            day=31
            year-=1
            print(f"previous day: {day}/{month}/{year}")
        elif month==1 and day in range(2,32):
            day-=1
            print(f"next day: {day}/{month}/{year}")
        elif month==12 and day in range(2,32):
            day-=1
            print(f"next day: {day}/{month}/{year}")
        elif month==12 and day==1:
            day=30
            month=11
            print(f"next day: {day}/{month}/{year}")
        else:
            day-=1
            print(f"previous day: {day}/{month}/{year}")
    else:
        if month==3 and day==1:
            month=2
            day=28
            print(f"previous day: {day}/{month}/{year}")
        elif month in month_list30 and day==1:
            month-=1
            day=30
            print(f"previous day: {day}/{month}/{year}")
        elif month in month_list31 and day==1:
            month-=1
            day=31
            print(f"previous day: {day}/{month}/{year}")
        elif month==1 and day==1:
            month=12
            day=31
            year-=1
            print(f"next day: {day}/{month}/{year}")
        elif month==1 and day in range(2,32):
            day-=1
            print(f"next day: {day}/{month}/{year}")
        elif month==12 and day in range(2,32):
            day-=1
            print(f"next day: {day}/{month}/{year}")
        elif month==12 and day==1:
            day=30
            month=11
            print(f"next day: {day}/{month}/{year}")
        else:
            day-=1
            print(f"previous day: {day}/{month}/{year}")
        

def main():
    month_list31=[1,3,5,6,10,12]
    month_list30=[2,4,7,8,9,11]
    if year%4==0 and year%100!=0 or year%400==0:
        print("năm hợp lệ \nnăm bạn nhập là năm nhuận")
        if  month in range(1,13):
            print("tháng hợp lệ")
            if month==2 and day in range(1,29):
                print("ngày hợp lệ")
        else:
            print("vui lòng nhập lại tháng")
    else:
        print("năm hợp lệ")
        if  month in range(1,13):
            print("tháng hợp lệ")
            if month==2 and day in range(1,30):
                print("ngày hợp lệ")
            elif month in month_list30 and day in range(1,31):
                print("ngày hợp lệ")
            elif day in range(1,32):
                print("ngày hợp lệ")
            else:
                print("ngày không hợp lệ, vui lòng nhập lại")
        else:
            print("tháng không hợp lệ, vui lòng nhập lại tháng")
        


'''day=int(input("nhập vào ngày: "))
month=int(input("nhập vào tháng: "))
year=int(input("nhập vào năm: "))'''
year=2024
for month in range(1,13):
    for day in range(1,32):
       nextday(day, month, year)



