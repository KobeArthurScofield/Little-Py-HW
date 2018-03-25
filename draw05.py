#charset: UTF-8

# Turtle Draw Image 5
# Kobe Arthur Scofield
# 2018-03-17
# Build 1
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.2
# Final edit: VSCode 1.21.1

import turtle
import math

ttdraw = turtle

def line_unit(lgth, angle):
    ttdraw.forward(lgth)
    ttdraw.backward(0.8*lgth)
    ttdraw.right(angle)
# End of line_unit

def line_draw(centposx, centposy, size, sides):
    anglez = 360 / sides
    drlgth = size
    ttdraw.penup()
    ttdraw.setposition(centposx, centposy)
    ttdraw.left(anglez)
    ttdraw.forward(drlgth / 5 / math.sin(anglez))
    ttdraw.right(90 + anglez)
    ttdraw.pendown()
    for loop in range(0 ,sides):
        line_unit(drlgth, anglez)
    ttdraw.penup()
    ttdraw.left(90)
    ttdraw.setposition(centposx, centposy)
# End of line_draw