from microbit import *
import tinybit

SPEED = 200
MOVE_TIME = 1200

display.show("H")
tinybit.car_run(SPEED)
sleep(MOVE_TIME)
tinybit.car_stop()
display.show(Image.HAPPY)
