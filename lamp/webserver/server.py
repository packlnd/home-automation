from flask import Flask, render_template, request, redirect
from pi import Pi

app = Flask(__name__)
global pi
pi = Pi(on=7, off=17)

@app.route("/turn_on")
def turn_on():
    #TODO: Authentication in header
    global pi
    pi.lamp_on()

@app.route("/turn_off")
def turn_off():
    #TODO: Authentication in header
    global pi
    pi.lamp_off()

if __name__ == "__main__":
    app.debug=True
    app.run()
