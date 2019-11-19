"""Snake, classic arcade game.

Excercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector


food = vector(0, 0)#绿色方块食物在中心点
snake = [vector(10, 0)]#10为红点位置，到达9宣布结束，8为可动范围
aim = vector(0, -10)#不不不不理解，测试后不懂什么逻辑
#测试更改变量   达不到   测试变量效果

def change(x, y):#蛇的方向，坐标系显示画面
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):#蛇头到达位置判断---存活  是否反骨--自己吃自己
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
#帮忙捋一下逻辑运算

def move():#身子移动位置
    "Move snake forward one segment."
    head = snake[-1].copy()#走一步身子就跟着走
    head.move(aim)#蛇头移动到的位置

    if not inside(head) or head in snake:#条件判断蛇头
        square(head.x, head.y, 9, 'red')
        update()
        return
    # 10为红点位置，到达9宣布结束，8为可动范围
    snake.append(head)#身子加头

##################

    if head == food:#条件判断蛇头碰到食物
        print('Snake:', len(snake))#则身子成长1
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:#如果不是就
        snake.pop(0)#不增加任何

    clear()
#固定不变的格式     并规定在范围9（包含）
    for body in snake:
        square(body.x, body.y, 9, 'black')#蛇全身都是黑

    square(food.x, food.y, 9, 'green')#食物都是绿
    update()
    ontimer(move, 100)#（移动步数计时器，100峰值）

setup(420, 420, 370, 0)#（长，宽，窗口所在显示界面）
hideturtle()#调用海龟库隐藏尖头
tracer(False)#不持续跟踪显示动作
listen()#海龟库按键接收传递
onkey(lambda: change(10, 0), 'Right')#右
onkey(lambda: change(-10, 0), 'Left')#左
onkey(lambda: change(0, 10), 'Up')#上
onkey(lambda: change(0, -10), 'Down')#下
move()#移动
done()#结束
