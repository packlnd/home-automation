from flask import Flask, render_template, request, redirect
from pi import lamp_on, lamp_off

app = Flask(__name__)
cal = None

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/turn_on")
def turn_on():
    lamp_on()

@app.route("/turn_off")
def turn_off():
    lamp_off()

if __name__ == "__main__":
    app.debug=True
    app.run()
