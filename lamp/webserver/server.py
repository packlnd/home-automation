from flask import Flask, request, jsonify, render_template
from pi import Pi
import os

app = Flask(__name__)
pi = Pi(on=17, off=27)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/on")
def on():
    #TODO: Authentication in header
    print "ON"
    pi.lamp_on()
    return jsonify({'status': 200})

@app.route("/off")
def off():
    #TODO: Authentication in header
    print "OFF"
    pi.lamp_off()
    return jsonify({'status': 200})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
