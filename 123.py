import turtle

import random

from tkinter.simpledialog import *

 

## 전역변수 선언 부분 ##

inStr = ''

swidth, sheight = 1400, 700
tX, tY, txtSize = [0] * 3
## 배경 이미지 설정
screen = turtle.Screen()
screen.bgpic("sky2.gif")

 

## 메인 함수 부분 ##

turtle.title('인간 관계론,데일 카네기')

turtle.shape('turtle')

turtle.setup(width = swidth, height = sheight )

turtle.screensize(swidth, sheight)

turtle.penup()

inStr = askstring('문자열 입력', "거북이 쓸 문자열을 입력")
tX = -600
tY = 220


for ch in inStr :

    
    
    if ch == '잘':
        txtSize = 25
    else:
        txtSize = 15
  

 

    turtle.goto(tX, tY)
  
 

    turtle.pencolor('white')

    turtle.write(ch, font=('1훈새마을운동 Regular', txtSize, 'bold'))
    tX += 50
    if ch == ' ':
        txtSize = 7
    if ch == '.' :
        tX = -600
        tY -= 40

turtle.goto(0, 0)
turtle.done()