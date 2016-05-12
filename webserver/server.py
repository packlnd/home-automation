from flask import Flask, request, jsonify, render_template
from pi import Pi
import alarm
import os
import util

app = Flask(__name__)
pi = Pi(on=27, off=22)
global lamp_status
lamp_status = False

@app.route("/")
def index():
    global lamp_status
    return render_template("index.html",data=lamp_status)

@app.route("/morning_alarm", methods=['POST'])
def morning():
    time = request.form['time']
    alarm = alarm.set_alarm(util.parse_time(time))
    logger.log_alarm(alarm)
    return jsonify({'alarms': alarm.get_alarms()})

@app.route("/remove_alarm", methods=['POST'])
def remove_alarm():
    alarm_id = request.form['id']
    alarm.remove_alarm(alarm_id, logger)
    return jsonify({'status': 200})

@app.route("/lamp_status")
def lamp_status():
    return jsonify({'status': lamp_status})

@app.route("/stats")
def stats():
    return jsonify(pi.get_stats())

@app.route("/on")
def on():
    #TODO: Authentication in header
    pi.lamp_on()
    global lamp_status
    lamp_status = True
    return jsonify({'status': 200})

@app.route("/off")
def off():
    #TODO: Authentication in header
    global lamp_status
    lamp_status = False
    pi.lamp_off()
    return jsonify({'status': 200})

if __name__ == "__main__":
    lamp_status = False
    app.run(debug=True, host='0.0.0.0')
