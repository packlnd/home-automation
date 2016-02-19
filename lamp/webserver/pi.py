import RPi.GPIO as GPIO

class Pi:
    def __init__(self,on,off):
        self.on = on
        self.off = off
        init_GPIOs()

    def init_pin(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    def init_GPIOs(self,pins):
        self.init_pin(self.on)
        self.init_pin(self.off)

    def lamp_on(self):
        self.simulate_button(self.on)

    def lamp_off(self):
        self.simulate_button(self.off)

    def simulate_button(self, btn):
        GPIO.output(btn, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(btn, GPIO.HIGH)
