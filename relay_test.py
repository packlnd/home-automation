#!/usr/bin/python
import RPi.GPIO as GPIO
import time,sys

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
    if len(sys.argv) < 1:
        print 'Usage: python relay_test pin1 pin2 pin3'
    pins = [int(s) for s in sys.argv]
    init_pins(pins)
    for _ in range(5):
        for p in pins:
            test_GPIO(p)
    GPIO.cleanup()

main()
