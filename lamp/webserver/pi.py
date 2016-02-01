import RPi.GPIO as GPIO

class Pi:
    def __init__(self,on,off):
        self.on = on
        self.off = off

    def init_GPIOs(self,pins):
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

    def lamp_on(self):
        GPIO.output(self.on, GPIO.LOW)
        GPIO.output(self.on, GPIO.HIGH)

    def lamp_off(self):
        GPIO.output(self.off, GPIO.LOW)
        GPIO.output(self.off, GPIO.HIGH)
