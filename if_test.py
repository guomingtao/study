# x=int(input("请输入一个整数："))
# if x < 0:
#     x = 0
#     print("Negative changed to zero")
# elif x == 0:
#     print("zero")
# elif x == 1:
#     print("Single")
# else:
#     print("more")

# words= ['cat','window','defenestrate']
# for w in words:
#     print(w,len(w))
# for w in words[:]:
#     if len(w) > 6:
#         words.insert(0,w)
# print(words)

# a,b =0,1
# while b <= 2000:
#     print(b,end=',')
#     a,b = b,a+b
# print()
#
# import os
# print(dir(os))
# import turtle as ttl
# ttl.title('我的画图')
# ttl.width(4)
# ttl.forward(200)
#
# ttl.right(90)
# ttl.pencolor('green')
# ttl.forward(100)
#
# ttl.right(90)
# ttl.pencolor("blue")
# ttl.forward(200)
#
# ttl.right(90)
# ttl.pencolor('red')
# ttl.forward(100)
#
# ttl.done()


import turtle as t


def hair():
    t.penup()
    t.goto(-50, 150)
    t.pendown()
    t.fillcolor('#a2774d')
    t.begin_fill()
    for j in range(10):
        t.setheading(60 - (j * 36))
        t.circle(-50, 120)
    t.end_fill()


def face():
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.fillcolor('#f2ae20')
    t.begin_fill()
    t.setheading(180)
    t.circle(85)
    t.end_fill()
    # 下巴
    t.circle(85, 120)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(85, 120)
    t.setheading(135)
    t.circle(100, 95)
    t.end_fill()


def ears(dir):
    t.penup()
    t.goto((0 - dir) * 30, 90)
    t.setheading(90)
    t.pendown()
    t.fillcolor('#f2ae20')
    t.begin_fill()
    t.circle(dir * 30)
    t.end_fill()

    t.penup()
    t.goto((0 - dir) * 40, 85)
    t.setheading(90)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(dir * 17)
    t.end_fill()


def nose():
    t.penup()
    t.goto(20, 0)
    t.setheading(90)
    t.pendown()
    t.fillcolor('#a2774d')
    t.begin_fill()
    t.circle(20)
    t.end_fill()


def eye(dir):
    t.penup()
    t.goto((0 - dir) * 30, 20)
    t.setheading(0)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(10)
    t.end_fill()


def mouth():
    t.penup()
    t.goto(0, 0)
    t.setheading(-90)
    t.pendown()
    t.forward(50)
    t.setheading(0)
    t.circle(80, 30)
    t.penup()
    t.goto(0, -50)
    t.setheading(180)
    t.pendown()
    t.circle(-80, 30)

# t.circle(50,120)
hair()
ears(1)
ears(-1)
face()
eye(1)
eye(-1)
mouth()
nose()
t.done()