#charset: UTF-8

# Turtle Draw Image 2
# Kobe Arthur Scofield (Lin Yaohua)
# 2018-03-16
# Build 7
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.2
# Final Editor: VSCode 1.21.1

import turtle
import math     # Sine required

ttdraw = turtle  #To make it easier to modify the code

# This function tries to draw a little unit in tiled-circled-style
# lgth:  length of the tile
# angle: to control where it goes
def tile_unit(lgth, anglea, angleb):
    ttdraw.forward(lgth)
    ttdraw.left(anglea)
    ttdraw.forward(lgth)
    ttdraw.left(angleb)
    ttdraw.forward(lgth)
    ttdraw.left(angleb)
# End of tile_unit

# This function tries to draw the whole image
# centpos: center position
# size:    radius of the image
# sides:   how many edges of the image
def tile_draw(centposx, centposy, size, sides):
    unitangle = 360 / sides         # Each unit's angle between
    hlfunitangle = unitangle / 2    # For turning
    length = 2 * size * math.sin((hlfunitangle/180)*math.pi)    # Edge's length
    ttdraw.penup()
    ttdraw.goto(centposx, centposy)
    ttdraw.left(hlfunitangle)     # Turn to 1st point
    ttdraw.forward(size)                # Then go to there
    ttdraw.right(90 + hlfunitangle + unitangle)   # Turtle, turn your head there!
    ttdraw.pendown()                    # Turtle climb
    for loop in range(0, sides):
        tile_unit(length, unitangle, 180 - unitangle)
    ttdraw.right(90 + unitangle)  # Turtle, turnback!
    ttdraw.penup()
    ttdraw.goto(centposx, centposy)   # Back to where it start
# End of tile_draw

# ttdraw.left(90)
# tile_draw(0, 0, 150, 8)
