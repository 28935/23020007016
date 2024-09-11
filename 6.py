num = int(input("please input num: "))
ii = True

if num < 2:
    ii = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            ii = False
            break

if ii:
    print("is")
else:
    print("isn't")
