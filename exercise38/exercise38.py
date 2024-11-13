def breakdown_money(n):
    count_5000 = 0
    count_2000 = 0
    count_1000 = 0

    while n >= 5000:
        n -= 5000
        count_5000 += 1
    while n >= 2000:
        n -= 2000
        count_2000 += 1
    while n >= 1000:
        n -= 1000
        count_1000 += 1
    
    return count_1000, count_2000, count_5000

n = int(input("Nhập số tiền (nghìn đồng, n > 5): "))
count_1000, count_2000, count_5000 = breakdown_money(n)
print(f"Phân tích tiền: {count_1000} tờ 1000 VNĐ, {count_2000} tờ 2000 VNĐ, {count_5000} tờ 5000 VNĐ")
