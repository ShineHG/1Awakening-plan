"""Bounce, a simple animation demo.

Exercises

1. Make the ball speed up and down.
2. Change how the ball bounces when it hits a wall.
3. Make the ball leave a trail.
4. Change the ball color based on position.
   Hint: colormode(255); color(0, 100, 200)

"""

from random import *
from turtle import *
from freegames import vector

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."#随机生成(-5, -3) or (3, 5)范围坐标系
    return (3 + random() * 2) * choice([1, -1])#返回动态反弹  动态模糊

ball = vector(0, 0)#起始点
aim = vector(value(), value())

def draw():#页面运作
    "Move ball and draw game."
    ball.move(aim)

    x = ball.x
    y = ball.y

    if x < -200 or x > 200:
        aim.x = -aim.x

    if y < -200 or y > 200:
        aim.y = -aim.y

    clear()#上面的draw      承上启下作用反应到画面进行
    goto(x, y)#相应的点
    dot(10)#球的大小


    ontimer(draw, 50)#动作速度

setup(420, 420, 370, 0)#（长，宽，窗口所在显示界面）
hideturtle()#调用海龟库隐藏尖头
tracer(False)#不持续跟踪显示动作
up()#持续运行
draw()#实时画面
done()#结束
