from flask import Flask, render_template, request, redirect

app = Flask(__name__)
cal = None

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/turn_on")
def turn_on():
    raise NotImplementedError

@app.route("/turn_off")
def turn_off():
    raise NotImplementedError

if __name__ == "__main__":
    app.debug=True
    app.run()
