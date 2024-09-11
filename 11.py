def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))
print(f"{num1}和{num2}的最大公约数是：{gcd(num1, num2)}")
