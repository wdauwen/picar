import RPi.GPIO as gpio
import time
import sys



#pin 7 =
#pin 11 =


gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)



gpio.output(7, True)
gpio.output(11, False)
gpio.output(13, False)
gpio.output(15, False)

time.sleep(2)
gpio.cleanup()
