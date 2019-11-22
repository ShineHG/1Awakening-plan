"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
from freegames import vector

def line(start, end):#鼠标点击的方向在坐标轴的范围描绘  线  完毕结束
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):#鼠标点击的方向在坐标轴的范围描绘  正方形 完毕结束
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):#循环填充方格颜色 正方形块
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):#圈对象，开始完成，结束停止
    "Draw circle from start to end."
    pass  # TODO

def rectangle(start, end):#矩形对象 ，开始完成，结束停止
    "Draw rectangle from start to end."
    pass  # TODO

def triangle(start, end):#三角形对象 ，开始完成，结束停止
    "Draw triangle from start to end."
    pass  # TODO

def tap(x, y):#线条对象，根据坐标系位置
    "Store starting point or draw shape."
    start = state['start']#根据标点点击位置 连接 点 成线条

    if start is None:#判断开始状态是否再进行连接第二个点
        state['start'] = vector(x, y)#第一个点连接第二个点位置
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

# 其他：成形状
#          形状=状态['形状']
#          结束=向量（x，y）位置连接
#          形状（开始，结束）完成结束
#          状态['开始'] =无  无连接结束
def store(key, value):#状态=键值对          点线面成形
    "Store value in state at key."#值存储键
    state[key] = value#状态键=值

state = {'start': None, 'shape': line}#状态=键值对（开始，无形成）（形成形状，线条）
setup(420, 420, 370, 0)#（长，宽，窗口所在显示界面）
onscreenclick(tap)#鼠标点击接收控制
listen()#海龟库按键接收传递
onkey(undo, 'u')#撤消
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')#线
onkey(lambda: store('shape', square), 's')#三角形
onkey(lambda: store('shape', circle), 'c')#圈
onkey(lambda: store('shape', rectangle), 'r')#矩形
onkey(lambda: store('shape', triangle), 't')
done()#结束
