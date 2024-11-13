import numpy as np

def round_number(x, precision):
    return np.round(x, precision)

x = float(input("Nhập số thực x: "))
precision = int(input("Nhập độ chính xác: "))
rounded_value = round_number(x, precision)
print(f"Số sau khi làm tròn: {rounded_value}")
