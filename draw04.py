#charset: UTF-8

# Turtle Draw Image 4
# Kobe Arthur Scofield
# 2018-03-17
# Build 2
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.2
# Final edit: VSCode 1.21.1

import turtle

ttdraw = turtle

# To draw a unit
def triangle_unit(lgth, angle):
    ttdraw.forward(lgth)
    ttdraw.left(120)
    ttdraw.forward(lgth)
    ttdraw.left(120)
    ttdraw.forward(lgth)
    ttdraw.left(120)
    ttdraw.forward(2*lgth/3)
    ttdraw.right(angle)
# End triangle_unit

# TO draw the whole image
def triangle_draw(centposx, centposy, size, sides):
    anglex = 360 / sides
    drlgth = size / 2
    ttdraw.penup()
    ttdraw.setposition(centposx, centposy)
    ttdraw.left(41.8)       # Can't find in the math module so just used calculator
    ttdraw.forward(drlgth)
    ttdraw.right(131.8)     # Like above
    ttdraw.pendown()
    for loop in range(0, sides):
        triangle_unit(drlgth, anglex)
    ttdraw.penup()
    ttdraw.left(90)
    ttdraw.setposition(centposx, centposy)
# End of triangle_draw
