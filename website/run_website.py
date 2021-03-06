"""
Run Flask website
"""

import os
from flask import Flask, render_template

app = Flask(__name__)
app._static_folder = os.path.abspath("static/")

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/login/")
def login():
    return "Login page"

if __name__ == '__main__':
    app.run()
