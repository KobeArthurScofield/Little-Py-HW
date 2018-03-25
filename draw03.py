#charset: UTF-8

# Turtle Draw Image 3
# Kobe Arthur Scofield
# 2018-03-16
# Build 4
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.2
# FInale edit: VSCode 1.21.1

import turtle
import math

ttdraw = turtle

def flag_unit(lgth, sideangle):
    ttdraw.forward(lgth * 2)
    ttdraw.right(120)
    ttdraw.forward(lgth)
    ttdraw.right(120)
    ttdraw.forward(lgth)
    ttdraw.left(240 - sideangle)
# End of flag_unit

def flag_draw(centposx, centposy, size, sides):
    mainangle = 360 / sides
    sidelg = (size / 4) / math.cos((mainangle/180) * math.pi)
    ttdraw.penup()
    ttdraw.setposition(centposx, centposy)
    ttdraw.left(mainangle / 2)
    ttdraw.forward(sidelg)
    ttdraw.pendown()
    ttdraw.right(90 - mainangle / 2)
    for i in range(0, sides):
        flag_unit(sidelg, mainangle)
    ttdraw.penup()
    ttdraw.right(mainangle * 2)
    ttdraw.goto(centposx, centposy)
#
