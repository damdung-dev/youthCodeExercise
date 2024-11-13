def rearrange_array(arr):
    odds = [x for x in arr if x % 2 != 0]
    zeros = [x for x in arr if x == 0]
    evens = [x for x in arr if x % 2 == 0 and x != 0]
    return odds + zeros + evens

def generate_array(n):
    return np.random.randint(-100, 101, size=n)

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

rearranged_arr = rearrange_array(arr)
print(f"Mảng sau khi sắp xếp lẻ lên đầu, chẵn xuống cuối, 0 ở giữa: {rearranged_arr}")
