from flask import Flask, render_template, request, redirect
from pi import Pi
import os
import haml
import haml.codegen
import mako.lookup

lookup = mako.lookup.TemplateLookup([os.path.dirname(__file__)],
        preprocessor=haml.preprocessor
)
app = Flask(__name__)
pi = Pi(on=7, off=17)

def render(html):
    return lookup.get_template(html).render_unicode()

@app.route("/")
def index():
    return render('templates/index.haml')

@app.route("/turn_on")
def turn_on():
    #TODO: Authentication in header
    pi.lamp_on()

@app.route("/turn_off")
def turn_off():
    #TODO: Authentication in header
    pi.lamp_off()

if __name__ == "__main__":
    app.debug=True
    app.run()
