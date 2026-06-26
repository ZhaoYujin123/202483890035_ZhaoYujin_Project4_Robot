from microbit import *
import tinybit

SPEED = 100
TURN_TIME = 700

display.show(Image.ARROW_W)
tinybit.car_spinleft(SPEED)
sleep(TURN_TIME)
tinybit.car_stop()
display.show(Image.HAPPY)
