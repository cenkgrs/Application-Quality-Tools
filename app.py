from flask import Flask, render_template, request, jsonify, make_response
from youtube_test import youtube_search, read_file
from readability import get_read
from performance import get_performance

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


@app.route('/readability-test', methods=["POST"])
def run_read():
    response = request.get_json()
    url = response["url"]
    data = get_read(url)
    print(data)

    return jsonify(data)


@app.route('/performance-test', methods=["POST"])
def run_performance_test():
    response = request.get_json()
    url = response["url"]

    data = get_performance(url)
    print(data)

    return jsonify(data)


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


if __name__ == '__main__':
    app.run()