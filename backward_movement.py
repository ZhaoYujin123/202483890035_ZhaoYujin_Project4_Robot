from microbit import *
import tinybit

SPEED = 100
MOVE_TIME = 2000

display.show(Image.ARROW_N)
tinybit.car_back(SPEED)
sleep(MOVE_TIME)
tinybit.car_stop()
display.show(Image.HAPPY)
