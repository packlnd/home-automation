from flask import Flask, render_template, request,redirect
import os
import haml
import haml.codegen
import mako.lookup

app = Flask(__name__)
lookup = mako.lookup.TemplateLookup([os.path.dirname(__file__)],
    preprocessor=haml.preprocessor
)

def render(html):
    return lookup.get_template(html).render_unicode()


@app.route('/')
def index():
    return render('templates/index.haml')

if __name__ == "__main__":
    app.debug=True
    app.run()
