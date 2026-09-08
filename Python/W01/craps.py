#游戏规则两粒骰子，第一次摇骰子，7 11 玩家获胜；2、3、12 庄家胜;其他点数重新摇
#第二次开始若摇出7点庄家胜利，和第一次相同玩家胜。
#本金1000，每次自由下注

import random


total = 1000
mark = 0  #0表示首次
while total > 0:
    if mark == 0:
        print(f"您的本金为{total}")
        money = int(input("请输入下注金额: "))
    input("请按x键摇骰子")
    x = random.randint(1,6)
    print(f"第一次摇骰子点数为{x}")
    input("请按x键摇骰子")
    y = random.randint(1,6)
    print(f"第二次摇骰子点数为{y}")


    if mark == 0 and (x + y == 7 or x + y == 11):
        print("玩家获胜")
        total += money
    elif mark == 0 and (x + y == 2 or x + y == 3 or x + y == 12):
        print("庄家获胜")
        total -= money
    elif mark != 0 and (x + y == 7):
        print("庄家获胜")
        total -= money
        mark = 0
    elif mark != 0 and (x + y == mark):
        print("玩家获胜")
        total += money
        mark = 0
    else:
        print("继续摇骰子")
        mark = x + y            
    if total <= 0:
        print("您的本金为0，游戏结束")
        break   