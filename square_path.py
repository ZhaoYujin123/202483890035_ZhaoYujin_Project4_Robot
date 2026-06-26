from microbit import *
import tinybit

SPEED = 100
FORWARD_TIME = 1000
TURN_TIME = 650
PAUSE_TIME = 300

display.show("P")

for step in range(4):
    tinybit.car_run(SPEED)
    sleep(FORWARD_TIME)
    tinybit.car_stop()
    sleep(PAUSE_TIME)

    tinybit.car_spinright(SPEED)
    sleep(TURN_TIME)
    tinybit.car_stop()
    sleep(PAUSE_TIME)

display.show(Image.HAPPY)
