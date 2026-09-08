x = input("请输入一个数字: ")
y  = 0
while True:
    if x=="q":
        break
    x = float(x)
    if x > 1:
        y = 3*x - 5
    elif -1<= x <= 1:
        y = x + 21
    else:
        y = 5*x + 3
    print(f"当x={x}时，y={y}")
    x = input("请输入一个数字: ")

    