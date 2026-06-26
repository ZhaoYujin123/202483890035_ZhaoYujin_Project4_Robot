from microbit import *
import tinybit

SPEED = 100
TURN_TIME = 700

display.show(Image.ARROW_E)
tinybit.car_spinright(SPEED)
sleep(TURN_TIME)
tinybit.car_stop()
display.show(Image.HAPPY)
