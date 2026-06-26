from microbit import *
import tinybit

SPEED = 100
MOVE_TIME = 2000

display.show(Image.ARROW_S)
tinybit.car_run(SPEED)
sleep(MOVE_TIME)
tinybit.car_stop()
display.show(Image.HAPPY)
