"""Connect Four

Exercises

1. Change the colors.
2. Draw squares instead of circles for open spaces.
3. Add logic to detect a full row.
4. Create a random computer player.
5. How would you detect a winner?

"""

from turtle import *
from freegames import line

turns = {'red': 'yellow', 'yellow': 'red'}#字典逻辑，状态值为键与值运行：红下一步操作为黄，黄下一步操作为红
state = {'player': 'yellow', 'rows': [0] * 8}#设置玩家点击后返回值为黄圈随后状态值跟随上面

def grid():
    "Draw Connect Four grid."
    bgcolor('light blue')#颜色设置为浅蓝色

    for x in range(-150, 200, 50):#（-150：从左竖计数3列， 200：从左竖第3列开始后4列， 50：竖间隔距离
        line(x, -200, x, 200)#（循环x，下橫4列，循环x，上橫4列）

    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            up()
            goto(x, y)
            dot(40, 'white')

    update()

def tap(x, y):#
    "Draw red or yellow circle in tapped row."
    player = state['player']
    rows = state['rows']

    row = int((x + 200) // 50)
    count = rows[row]

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    up()
    goto(x, y)
    dot(40, player)
    update()

    rows[row] = count + 1
    state['player'] = turns[player]

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(tap)
done()
