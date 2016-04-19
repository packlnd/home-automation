from flask import Flask, request, jsonify, render_template
from pi import Pi
import os

# Hi Vincent and Gabriel

app = Flask(__name__)
pi = Pi(on=27, off=22)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/on")
def on():
    #TODO: Authentication in header
    pi.lamp_on()
    return jsonify({'status': 200})

@app.route("/off")
def off():
    #TODO: Authentication in header
    pi.lamp_off()
    return jsonify({'status': 200})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
