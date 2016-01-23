#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def init_pins(pins):
    for i in pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

def test_GPIO(pin_no):
    timeout=1
    GPIO.output(pin_no, GPIO.LOW)
    time.sleep(timeout)
    GPIO.output(pin_no, GPIO.HIGH)
    time.sleep(timeout)

def main():
    GPIO.setmode(GPIO.BCM)
    pins = [17, 27]

    init_pins(pins)

    for _ in range(5):
        for p in pins:
            test_GPIO(p)
    GPIO.cleanup()
