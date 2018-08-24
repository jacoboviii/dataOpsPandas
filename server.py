import os, sys
from flask import Flask, url_for, render_template
from data import Articles
import webview

server = Flask(__name__)
server.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1  # disable caching

@server.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

# Import temporary data
Articles = Articles()

@server.route('/')
def index():
    return render_template('home.html')

@server.route('/about')
def about():
    return render_template('about.html')

@server.route('/upload')
def upload():
    return render_template('upload.html')

def run_server():
    server.run(host="127.0.0.1", port=5100, threaded=True)
    # server.run(debug=True)

if __name__ == "__main__":
    run_server()
