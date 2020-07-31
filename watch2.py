#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#   Reed Switch Watcher. Continious Looping.
pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:

	channel = GPIO.wait_for_edge(pin, GPIO.RISING, timeout=1000)
	time.sleep(2)
    if channel is not None: 
	    print("Switch is on")
	time.sleep(1)

	channel = GPIO.wait_for_edge(pin, GPIO.FALLING, timeout=1000)
	time.sleep(1)
    if channel is None: 
	    print("Switch is off")