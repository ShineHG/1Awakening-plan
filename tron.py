"""Tron, classic arcade game.

Exercises

1. Make the tron players faster/slower.
2. Stop a tron player from running into itself.
3. Allow the tron player to go around the edge of the screen.
4. How would you create a computer player?

"""

from turtle import *
from freegames import square, vector
#p1aim=红色
#p2aim=蓝色

#红
p1xy = vector(-100, 0)#物质守恒定律
p1aim = vector(4, 0)#调整线的形状
p1body = set()#返回新的集合对象。


#蓝
p2xy = vector(100, 0)#物质守恒定律
p2aim = vector(-4, 0)#调整线的形状
p2body = set()#返回新的集合对象

def inside(head):
    "Return True if head inside screen."
    return -200 < head.x < 200 and -200 < head.y < 200
#广义表读取指定范围内容执行   显示到达位置
def draw():
    "Advance players and draw game."
    p1xy.move(p1aim)#红色移动
    p1head = p1xy.copy()#路径复制痕迹

    p2xy.move(p2aim)#蓝色移动
    p2head = p2xy.copy()#路径复制痕迹

    if not inside(p1head) or p1head in p2body:#检测判断红色是否碰到我内部
        print('Player blue wins!')#蓝色获胜
        return

    if not inside(p2head) or p2head in p1body:#检测判断蓝色是否碰到我内部
        print('Player red wins!')#红色获胜
        return

    p1body.add(p1head)#持续增长
    p2body.add(p2head)#持续增长

    square(p1xy.x, p1xy.y, 3, 'red')#宽度
    square(p2xy.x, p2xy.y, 3, 'blue')#宽度
    update()#更新接收
    ontimer(draw, 50)#线条运行速度

setup(420, 420, 370, 0)#（长，宽，窗口所在显示界面）
hideturtle()#调用海龟库隐藏尖头
tracer(False)#不持续跟踪显示动作
listen()#海龟库按键接收传递
onkey(lambda: p1aim.rotate(90), 'a')#红上90度方向
onkey(lambda: p1aim.rotate(-90), 'd')#红下90度方向
onkey(lambda: p2aim.rotate(90), 'j')#蓝上90度方向
onkey(lambda: p2aim.rotate(-90), 'l')#蓝下90度方向
draw()##画面显示
done()#结束