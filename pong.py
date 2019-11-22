"""Pong, classic arcade game.

Exercises

1. Change the colors.
2. What is the frame rate? Make it faster or slower.
3. Change the speed of the ball.
4. Change the size of the paddles.
5. Change how the ball bounces off walls.
6. How would you add a computer player?
6. Add a second ball.

"""

from random import choice, random
from turtle import *
from freegames import vector

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."#随机生成(-5, -3) or (3, 5)范围坐标系
    return (3 + random() * 2) * choice([1, -1])#返回动态反弹  动态模糊

ball = vector(0, 0)#起始点
aim = vector(value(), value())
state = {1: 0, 2: 0}#球的运动状态

def move(player, change):#玩家移动球拍位置
    "Move player position by change."
    state[player] += change

def rectangle(x, y, width, height):
    "Draw rectangle at (x, y) with given width and height."
    up()#更新
    goto(x, y)#相应的点
    down()#向前？？运动轨迹？？
    begin_fill()#？？？
    for count in range(2):#球拍的作用力循环平衡，
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw():
    "Draw game and move pong ball."
    clear()
    rectangle(-200, state[1], 10, 50)#球拍设置的长距离，
    rectangle(190, state[2], 10, 50)#球拍设置的长距离，

    ball.move(aim)#球移动
    x = ball.x
    y = ball.y

    up()#接收更新
    goto(x, y)#相应的点
    dot(10)#球的大小
    update()#持续运行

#承上启下作用反应到画面进行
    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    ontimer(draw, 50)#动作速度

setup(420, 420, 370, 0)#（长，宽，窗口所在显示界面）
hideturtle()#调用海龟库隐藏尖头
tracer(False)#不持续跟踪显示动作
listen()#海龟库按键接收传递
onkey(lambda: move(1, 20), 'w')#左上
onkey(lambda: move(1, -20), 's')#左下
onkey(lambda: move(2, 20), 'i')#右上
onkey(lambda: move(2, -20), 'k')#右下
draw()#实时画面
done()#结束
