def lunar_year(year):
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
    
    can_index = (year + 6) % 10
    chi_index = (year + 8) % 12
    return f"{can[can_index]} {chi[chi_index]}"

year = int(input("Nhập năm dương lịch: "))
lunar_name = lunar_year(year)
next_same_lunar_year = year + 60

print(f"{year} - {lunar_name}")
print(f"Năm dương lịch kế tiếp có cùng tên âm lịch: {next_same_lunar_year} - {lunar_year(next_same_lunar_year)}")
