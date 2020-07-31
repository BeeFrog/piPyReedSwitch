#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#   Reed Switch Watcher. Continious Looping.
pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(pin, GPIO.RISING)  # add rising edge detection on a channel

start = time.time()
while True:
    if GPIO.event_detected(pin):
        print('switch triggered')    
    if time.time() - start > 5:
        print('Timeout')
    time.sleep(0.0001)