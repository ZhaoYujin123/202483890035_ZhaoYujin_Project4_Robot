from microbit import *
import tinybit

SPEED = 60
MOVE_TIME = 1500

display.show("L")
tinybit.car_run(SPEED)
sleep(MOVE_TIME)
tinybit.car_stop()
display.show(Image.HAPPY)
