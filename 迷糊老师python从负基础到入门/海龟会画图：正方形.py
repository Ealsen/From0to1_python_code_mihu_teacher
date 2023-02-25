import turtle

""" 
turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)
 """
i = 0
while i < 4 :
    turtle.forward(100)
    turtle.left(90)
    i += 1

# 窗口保持
turtle.done()
# 或 turtle.mainloop()