# -*- coding: utf-8 -*-
# 电脑出数字，小朋友猜数字
# 另外一个 小朋友出数字，电脑猜数字
import random # 大脑 产生随机数

secret = random.randint(1,100)# 电脑出的一个整数，范围1~99
guess = 0 # 小朋友猜的数字
tries = 0 # 尝试的次数

print("小朋友，你将我6次机会猜出我出的数字，范围在1~99之间，开始吧")

# 做游戏，游戏结束的两个条件，1.小朋友猜对了；2，6次机会用完了
while guess != secret and tries < 6:  # 只要没猜对且机会没用完，游戏一直进行
    guess = input("小朋友这次猜多少?")  # 获取小朋友猜的数字 
    if guess < secret:  # 猜小了
        print("小了")
    elif guess > secret:# 猜大了
        print("大了")
    tries = tries + 1
        
if guess == secret:
    print("恭喜你，小朋友，你猜对了")
else:
    print("不要灰心，小朋友，看看答案是多少吧 ")
    print(secret)
