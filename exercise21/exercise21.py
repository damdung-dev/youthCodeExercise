import numpy as np

# Input the necessary information
diem_chuan = float(input("Nhập điểm chuẩn của hội đồng: "))
diem_mon_1 = float(input("Nhập điểm môn 1 của thí sinh: "))
diem_mon_2 = float(input("Nhập điểm môn 2 của thí sinh: "))
diem_mon_3 = float(input("Nhập điểm môn 3 của thí sinh: "))
khu_vuc = input("Nhập khu vực của thí sinh (A, B, C, hoặc x nếu không thuộc khu vực ưu tiên): ")
doi_tuong = input("Nhập đối tượng dự thi (1, 2, 3, hoặc 0 nếu không thuộc đối tượng ưu tiên): ")

# Define priority points for regions and categories
khu_vuc_diem = {
    'A': 2.0,
    'B': 1.0,
    'C': 0.5,
    'x': 0.0
}

doi_tuong_diem = {
    '1': 2.5,
    '2': 1.5,
    '3': 1.0,
    '0': 0.0
}

# Calculate total score
diem_uu_tien = khu_vuc_diem.get(khu_vuc, 0.0) + doi_tuong_diem.get(doi_tuong, 0.0)
diem_tong = diem_mon_1 + diem_mon_2 + diem_mon_3 + diem_uu_tien

# Determine if the student passes
if diem_mon_1 > 0 and diem_mon_2 > 0 and diem_mon_3 > 0 and diem_tong >= diem_chuan:
    print(f"Thí sinh đậu! Tổng điểm đạt được: {diem_tong}")
else:
    print(f"Thí sinh rớt. Tổng điểm đạt được: {diem_tong}")
