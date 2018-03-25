#charset: UTF-8

# Turtle Draw Image 1
# Kobe Arthur Scofield (Lin Yaohua)
# 2018-03-15
# Build 8
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.2
# Final edit: VSCode 1.21.1

import turtle
import math     # Sin function required
# import time

ttdraw = turtle  # Something seems wrong with the Intellisense. To reduce the work of code replacement.

# To draw a unit of the chrysanthemum
# midllg:    the length of the chrysanthemum unit
# outbndlg:  the width of the chrysanthemum unit
# ctrlangle: a main control turning angle
def crstmum_unit(midllg, outbndlg, ctrlangle):
    ttdraw.forward(midllg)
    ttdraw.right(90)          # Turn on the corner
    ttdraw.forward(outbndlg)
    ttdraw.right(90)          # Turn on the corner again
    ttdraw.forward(midllg)
    ttdraw.left(180 - ctrlangle)    # Reset the direction
# End of crstmum_unit

# To draw a chrysanthemum
# centpos:   the center of the chrysanthemum
# sidecount: the number of the unit of the chrysanthemum
# centrd:    blanking area radius
# boundrd:   chrysanthemum radius
def crstmum_draw(centposx, centposy, sidecount, centrd, boundrd):
    centwalk = boundrd - centrd     # width of the chrysanthemum unit
    if (180 % sidecount == 0):      # Floating minor error ;-)
        print("Everything should be OK.")
    else:
        print("Image can be drawed but may be have some error.")
    constUnitAngle = 360 / sidecount                        # Turning angle of the chrysanthemum unit
    constHlfAngle = constUnitAngle / 2                      # Required in actual drawing
    bndlg = math.sin((constHlfAngle/180)*math.pi)*centrd*2  # Width of the chrysanthemum unit
    ttdraw.penup()                                          # Turtle, don't climb on the floor!
    ttdraw.setposition(centposx, centposy)            # Where is the center of the chrysanthemum? 
    ttdraw.left(constHlfAngle)                        # Turning toward the drawing point
    ttdraw.forward(centrd)                            # Run through the blangking area
    ttdraw.right(constHlfAngle)                       # Start Draw
    ttdraw.pendown()
    for loop in range(0, sidecount):                        # Loop drawing with feature fixed
        crstmum_unit(centwalk, bndlg, constUnitAngle)
    ttdraw.penup()
    ttdraw.goto(centposx, centposy)
    print("Draw complete.")
# End of crstmum_draw

# ttdraw.left(90)
# crstmum_draw(0, 0, 10, 50, 150)
# time.sleep(4)
