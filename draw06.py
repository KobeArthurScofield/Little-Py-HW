#charset: UTF-8

# Turtle Draw Image 6
# Kobe Arthur Scofield
# 2018-03-17
# Build 1
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.2
# Final edit: VSCode 1.21.1

import turtle
import math

ttdraw = turtle

def crsscrstmum_unit(lgth, wdth, drangle):
    ttdraw.forward(lgth)
    ttdraw.right(90)
    ttdraw.forward(wdth)
    ttdraw.right(90)
    ttdraw.forward(lgth)
    ttdraw.left(drangle)
# End of crsscrstmum_unit

def crsscrstmum_draw(centposx, centposy, size, sides, centrd):
    angley = 360 / sides
    unitlgth = size - centrd
    unitwdth = 2 * math.sin(angley) * centrd        # get how wide shou the chrysanthemum be
    ttdraw.penup()
    ttdraw.setposition(centposx, centposy)
    ttdraw.left(angley)
    ttdraw.forward(centrd)
    ttdraw.right(angley)
    ttdraw.pendown()
    for loop in range(0, sides):
        crsscrstmum_unit(unitlgth, unitwdth, angley)
    ttdraw.penup()
    ttdraw.setposition(centposx, centposy)
# End of crsscrstmum_draw
