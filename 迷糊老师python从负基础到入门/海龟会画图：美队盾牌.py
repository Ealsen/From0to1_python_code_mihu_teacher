import turtle
import time

# 绘制大圆
turtle.pensize(10)
turtle.pencolor('red')
turtle.circle(105)

# 提笔
turtle.left(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.right(90)

# 绘制小园并填充蓝色
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(55)
turtle.end_fill()

# 绘制五角星并填充至小圆里
turtle.pensize(1)
turtle.pencolor('white')
turtle.fillcolor('white')

turtle.penup()
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(48)
turtle.left(180)
turtle.pendown()

turtle.begin_fill()
i = 0
while i < 5 :
    turtle.forward(100)
    turtle.right(144)
    i += 1
turtle.end_fill()

# 隐藏海龟
turtle.hideturtle()

# 窗口保持
turtle.done()
# 或 turtle.mainloop()
