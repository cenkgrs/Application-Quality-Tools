from flask import Flask, render_template, request, jsonify
from youtube_test import youtube_search, read_file

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


@app.route('/selenium-test', methods=["POST"])
def run_test():

    response =  request.get_json()
    print(response)

    if response["type"] == "youtube":
        data = youtube_search()
        print(data)
        return jsonify(data)

    return "success"


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == '__main__':
    app.run()