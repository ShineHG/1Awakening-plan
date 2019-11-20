"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.

"""

from random import *
from turtle import *
from freegames import vector
#205高度峰值，204可动，暂且定为200
bird = vector(0, 0)#鸟的起始点
balls = []#黑球范围

def tap(x, y):#鼠标操作点击响应
    "Move bird up in response to screen tap."
    up = vector(0, 30)#向上30高度显示
    bird.move(up)#向上运动

def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200
#定点位置返回数据-200  小于    ##########不不不不不不理解

def draw(alive):#存活有效位置
    "Draw screen objects."#不碰到黑球的
    clear()

    goto(bird.x, bird.y)#鸟在坐标系显示的位置？？？？

    if alive:#10号大小的球  要么活着
        dot(10, 'green')#绿色存活正常
    else:# 要么终止
        dot(10, 'red')#红色为结束

    # 20号大小的黑色球
    for ball in balls:#不断随机出现中
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()#持续运作

def move():
    "Update object positions."
    bird.y -= 5#操作鸟球的下落运动的速度

    for ball in balls:
        ball.x -= 3#黑球的前进速度

    if randrange(10) == 0:#随机出黑球的数量  越低难度高
        y = randrange(-199, 199)#黑球的（上，下）方向出现
        ball = vector(199, y)#出生地的位置100为中间，199为最右边
        balls.append(ball)#黑球的可否循环出现的参数

    while len(balls) >0 and not inside(balls[0]):
        balls.pop(0)
##########不不不不不不理解，更改与删除没见着反应
    if not inside(bird):
        draw(False)
        return
    ##########不不不不不不理解

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return
    ##########不不不不不不理解

    draw(True)#画面返回
    ontimer(move, 50)#鸟球的下落速度重力，整体游戏速度加快控制

setup(420, 420, 370, 0)#（长，宽，窗口所在显示界面）
hideturtle()#调用海龟库隐藏尖头
up()#持续运作
tracer(False)#不持续跟踪显示动作
onscreenclick(tap)#点击 返回执行
move()#移动
done()#结束
