from flask import Flask, render_template, request, redirect

app = Flask(__name__)
cal = None

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug=True
    app.run()
