#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#   Reed Switch Watcher. Continious Looping.
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:

	GPIO.wait_for_edge(11, GPIO.RISING)
	time.sleep(2)
	print("Switch triggered on")	
	time.sleep(1)

	GPIO.wait_for_edge(11, GPIO.FALLING)
	time.sleep(2)
	print("Switch triggered off")	
	time.sleep(1)