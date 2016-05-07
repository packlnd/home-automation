from flask import Flask, request, jsonify, render_template
from pi import Pi
import alarm
import os

app = Flask(__name__)
pi = Pi(on=27, off=22)
global status
status = False

@app.route("/")
def index():
    return render_template("index.html",data=status)

@app.route("/morning_alarm", methods=['POST'])
def morning():
    time = request.args.get('time','')
    print time
    alarm.set_alarm(time)
    return jsonify({'alarms': alarm.get_alarms()})

@app.route("/remove_alarm", methods=['POST'])
def remove_alarm():
    alarm_id = request.args.get('id','')
    alarm.remove_alarm(alarm_id)
    return jsonify({'status': 200})

@app.route("/status")
def status():
    return jsonify({'status': status})

@app.route("/stats")
def stats():
    return jsonify(pi.get_stats())

@app.route("/on")
def on():
    #TODO: Authentication in header
    pi.lamp_on()
    global status
    status = True
    return jsonify({'status': 200})

@app.route("/off")
def off():
    #TODO: Authentication in header
    global status
    status = False
    pi.lamp_off()
    return jsonify({'status': 200})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
