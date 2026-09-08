#猜数字游戏
import random
number = random.randint(1, 100)
guess = int(input("请输入一个1到100之间的整数: "))
count = 0;
while guess != number:
    count += 1
    if guess < number:
        print("太小了，请再试一次。")
    else:
        print("太大了，请再试一次。")
    guess = int(input("请输入一个1到100之间的整数: "))
print("恭喜你，猜对了！答案是:", number)    
print("你总共猜了", count, "次。")