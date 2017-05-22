# -*- coding:utf-8 -*-

sex = input("input your gender:")
if sex == "girl":
    print("I would like to have a little monkey")
elif sex == "man":
    print("Going to homosexual!.....")
else:
    print("pervert")


#猜lucky number；
#猜的数字比你的小，提示给大一点
#猜的数字比你的大，提示给小一点
#刚好，则为lucky
lucky_number = 9
lucky = -1
while lucky_number != lucky:
    lucky = int(input("Please give your lucky number"))
    if lucky < lucky_number:
        print("your number is smaller")
    elif lucky > lucky_number:
        print("your number is bigger")
print("you are lucky man!")
