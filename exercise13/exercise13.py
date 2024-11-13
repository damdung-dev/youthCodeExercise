from functools import cache
@cache

def ngaytrongtuan(dayofweek):
    if dayofweek==0:
        print("sunday")
    elif dayofweek==1:
        print("monday")
    elif dayofweek==2:
        print("tuesday")
    elif dayofweek==3:
        print("wednesday")
    elif dayofweek==4:
        print("thursday") 
    elif dayofweek==5:
        print("friday")
    elif dayofweek==6:
        print("saturday")
    else:
        print("error")
def day_check(day):
    if day in range(1,29) or range(1,28):
        print("ngày hợp lệ")
        return 1
    else:
        print("vui lòng nhập lại tháng")

def main():
    day=int(input("nhập vào ngày: "))
    month=int(input("nhập vào tháng: "))
    year=int(input("nhập vào năm: "))
    month_list=[2,4,6,8,9,11]
    if year%4==0 and year%100!=0 or year%400==0:
        print("năm hợp lệ \nnăm bạn nhập là năm nhuận")
        if  month in range(1,13):
            print("tháng hợp lệ")
            if month==2 and day in range(1,29):
                print("ngày hợp lệ")
                year1=year-((14-month)/12)
                month1=month+12*((14-month)/12)-2
                dayofweek=(int((day+year1+year1/4-year1/100+year1/400+(31*month1)/12)%7))
                print(dayofweek)
        else:
            print("vui lòng nhập lại tháng")
    else:
        print("năm hợp lệ")
        if  month in range(1,13):
            print("tháng hợp lệ")
            if month==2 and day in range(1,30):
                print("ngày hợp lệ")
                year1=year-((14-month)/12)
                month1=month+12*((14-month)/12)-2
                dayofweek=(int((day+year1+year1/4-year1/100+year1/400+(31*month1)/12)%7))
                print(dayofweek)
            elif month in month_list and day in range(1,31):
                print("ngày hợp lệ")
                year1=year-((14-month)/12)
                month1=month+12*((14-month)/12)-2
                dayofweek=(int((day+year1+year1/4-year1/100+year1/400+(31*month1)/12)%7))
                print(dayofweek)
            elif day in range(1,32):
                print("ngày hợp lệ")
                year1=year-((14-month)/12)
                month1=month+12*((14-month)/12)-2
                dayofweek=(int((day+year1+year1/4-year1/100+year1/400+(31*month1)/12)%7))
                print(dayofweek)
            else:
                print("ngày không hợp lệ, vui lòng nhập lại")
        else:
            print("tháng không hợp lệ, vui lòng nhập lại tháng")
    ngaytrongtuan(dayofweek)
main()

