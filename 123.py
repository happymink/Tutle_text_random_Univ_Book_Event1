import turtle

import random

from tkinter.simpledialog import *

 

## 전역변수 선언 부분 ##

inStr = ''

swidth, sheight = 1500, 700
tX, tY, txtSize = [0] * 3
# screen = turtle.Screen()
# screen.bgpic("background.jpg")
# screen.update()

 

## 메인 함수 부분 ##

turtle.title('거북이 글자쓰기')

turtle.shape('turtle')

turtle.setup(width = swidth, height = sheight )

turtle.screensize(swidth, sheight)

turtle.penup()



inStr = askstring('문자열 입력', "거북이 쓸 문자열을 입력")
tX = -550
tY = 200
txtSize = 50

for ch in inStr :

    
    r = random.random(); g = random.random(); b = random.random();
    if ch == '잘':
        txtSize = 50
    else:
        txtSize = 30
    

 

    turtle.goto(tX, tY)
  
 

    turtle.pencolor((0,0,0))

    turtle.write(ch, font=('1훈새마을운동 Regular', txtSize, 'bold'))
    tX += 50

    if ch == '.' :
        tX = -550
        tY -= 55

turtle.goto(-550, 300)
turtle.done()