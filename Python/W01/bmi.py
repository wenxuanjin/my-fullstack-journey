#BMI计算器
weight = float(input("请输入您的体重(公斤): "))   
height = float(input("请输入您的身高(米): ")) 
bmi = weight / (height ** 2)
print("您的BMI指数为: %.2f" % bmi)
if bmi < 18.5:
    print("体重过轻")
elif 18.5 <= bmi < 24:
    print("体重正常")
elif 24 <= bmi < 28:
    print("体重过重")
else:
    print("肥胖")   
