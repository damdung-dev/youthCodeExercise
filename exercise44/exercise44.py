def solid_isosceles_triangle(height):
    for i in range(height):
        print(" " * (height - i - 1) + "* " * (i + 1))

def hollow_isosceles_triangle(height):
    for i in range(height):
        if i == height - 1:
            print("* " * (2 * height - 1))
        else:
            print(" " * (height - i - 1) + "* " + "  " * (i - 1) + ("*" if i > 0 else ""))

height = int(input("Nhập chiều cao n: "))
print("\nTam giác cân đặc:")
solid_isosceles_triangle(height)
print("\nTam giác cân rỗng:")
hollow_isosceles_triangle(height)
