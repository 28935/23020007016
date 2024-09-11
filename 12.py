def print_triangle(height):
    for i in range(height):
        print('*' * (i + 1))

triangle_height = int(input("请输入三角形的高度："))
print_triangle(triangle_height)
