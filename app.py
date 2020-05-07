from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/selenium')
def selenium():
    return render_template("sel_tool.html")


@app.route('/readability')
def readability():
    return render_template("readability.html")


if __name__ == '__main__':
    app.run()