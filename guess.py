"""Guess a number within a range.

Exercises

1. Change the range to be from 0 to 1,000,000.
2. Can you still guess the number?
3. Print the number of guesses made.
4. Limit the number of guesses to the minimum required.

"""

from random import randint

start = 1#1起始点
end = 100#100封顶
value = randint(start, end)#开始结束键  开关

print(value)#触发开始
print("I'm thinking of a number between", start, "and", end)
#低开始，高结束，继续选择
guess = None
#超出范围结束
while guess != value:
    text = input("Guess the number: ")#提示输入 你所猜测的数字
    guess = int(text)#提示猜测= 接收（数字）

    if guess < value:#判断数字为低输出提示 Higher更高的数字
        print("Higher.")
    elif guess > value:#判断数字为高输出提示 Lower更小的数字
        print("Lower.")

print("Congratulations! You guessed the right answer:", value)
#输出（“恭喜！您猜对了答案：”，结束）