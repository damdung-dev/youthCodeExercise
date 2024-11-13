from functools import cache
@cache

def time_difference(h1, m1, s1, h2, m2, s2):
    t1 = h1 * 3600 + m1 * 60 + s1
    t2 = h2 * 3600 + m2 * 60 + s2
    total_seconds = abs(t2 - t1)
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

h1=int(input("nhập vào giờ 1:"))
m1=int(input("nhập vào phút 1:"))
s1=int(input("nhập vào giây 1:"))
h2=int(input("nhập vào giờ 2:"))
m2=int(input("nhập vào phút 2:"))
s2=int(input("nhập vào giây 2:"))
print(f"hiệu thời gian: {time_difference(h1,m1,s1,h2,m2,s2)}")

