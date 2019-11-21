"""Fidget, inspired by fidget spinners.

Exercises

1. Change the spinner pattern.
2. Respond to mouse clicks.
3. Change its acceleration.
4. Make it go forwards and backwards.

"""

from turtle import *

state = {'turn': 0}#无动作静止

def spinner():
    "Draw fidget spinner."
    clear()#明确方向
    angle = state['turn'] / 10
    right(angle)#只向右每次转10幅度
    forward(100)#三个点牵引力必须相同，则会静止
    dot(120, 'red')#红球大小
    back(100)#三个点牵引力必须相同，则会静止
    right(120)#右方向下120显示
    forward(100)#三个点牵引力必须相同，则会静止
    dot(120, 'green')#绿球大小
    back(100)#三个点牵引力必须相同，则会静止
    right(120)#右方向下120显示
    forward(100)#三个点牵引力必须相同，则会静止
    dot(120, 'blue')#蓝球大小
    back(100)#三个点牵引力必须相同，则会静止  出力为蓝球方向
    right(120)#右方向下120显示
    update()#更新状态

def animate():
    "Animate fidget spinner."
    if state['turn'] > 0:#检测是否有操作空格运动
        state['turn'] -= 1#每操作1次反应、1

    spinner()
    ontimer(animate, 20)#提升 根据幅度 得以惯性运动实现

def flick():
    "Flick fidget spinner."
    state['turn'] += 10#提升阻力减少

setup(420, 420, 370, 0)#（长，宽，窗口所在显示界面）
hideturtle()#调用海龟库隐藏尖头
tracer(False)#不持续跟踪显示动作
width(10)#黑支架的宽度调整
onkey(flick, 'space')#空格  操作反应
listen()#海龟库按键接收传递
animate()#海龟库动画 移动显示
done()#结束
