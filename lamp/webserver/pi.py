import RPi.GPIO as GPIO
import time
from logger import Logger

GPIO.setmode(GPIO.BCM)
class Pi:
    def init_pin(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    def init_GPIOs(self):
        self.init_pin(self.on)
        self.init_pin(self.off)

    def __init__(self,on,off):
        self.on = on
        self.off = off
        self.logger = Logger()
        self.init_GPIOs()

    def simulate_button(self, btn):
        GPIO.output(btn, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(btn, GPIO.HIGH)

    def lamp_on(self):
        self.logger.log_on()
        self.simulate_button(self.on)

    def lamp_off(self):
        self.logger.log_off()
        self.simulate_button(self.off)

    def get_stats(self):
        return self.logger.get_stats()
