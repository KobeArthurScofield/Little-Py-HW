#charset: UTF-8

# Turtle Draw main file
# Kobe Arthur Scofield
# 2018-03-15
# Build 1
# Python: Anaconda3_64 5.0.0.0 (Python 3.6.2)
# IDE: MSVS2017_Community 15.6.2

import turtle
import time

import draw01
import draw02
import draw03
import draw04
import draw05
import draw06

ttdraw = turtle

ttdraw.left(90)
draw01.crstmum_draw(-300, 150, 10, 50 * 2 / 3, 100)
draw02.tile_draw(0, 150, 100, 8)
draw04.triangle_draw(-300, -150, 100, 8)
draw05.line_draw(0, -150, 100, 8)
draw06.crsscrstmum_draw(300, -150, 100, 8, 20)
draw03.flag_draw(300, 150, 75, 5)
time.sleep(20)