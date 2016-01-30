from flask import Flask, render_template, request, redirect
from pi import lamp_on, lamp_off

app = Flask(__name__)

@app.route("/turn_on")
def turn_on():
    #TODO: Authentication in header
    lamp_on()

@app.route("/turn_off")
def turn_off():
    #TODO: Authentication in header
    lamp_off()

if __name__ == "__main__":
    app.debug=True
    app.run()
