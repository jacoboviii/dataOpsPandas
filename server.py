from flask import Flask, render_template, flash, redirect, url_for, request, jsonify, send_file
from app import pdProcess, pdDownload
from wtforms import StringField, TextAreaField, PasswordField, validators
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
import traceback
import logging

server = Flask(__name__)
server.secret_key = 'secretkey123'
server.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1  # disable caching
pdGroupObject = None

@server.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

@server.route('/')
def index():
    return render_template('home.html')

@server.route('/about')
def about():
    return render_template('about.html')

class UploadForm(FlaskForm):
    upload = FileField('', validators=[
        FileRequired(),
        FileAllowed(['csv', 'xls', 'xlsx'], 'Please select an excel file.')
    ])

@server.route('/upload')
def upload():
    form = UploadForm()
    return render_template('upload.html', form=form)

@server.route('/process', methods=['POST'])
def process():
    form = UploadForm()   
    if request.method == 'POST' and form.validate_on_submit():
        inputfile = form.upload.data

        try:
            # Assign global value
            global pdGroupObject
            pdGroupObject = pdProcess(inputfile)
        except Exception as e:
            # Logs the error appropriately and send error message to client
            logging.error(traceback.format_exc())
            return jsonify(errors={'file':'Please select the correct excel file.'})
        # Send success message if OK
        return jsonify(data={'success': 'File successfully processed!'})
    # Send form errors to client
    return jsonify(errors=form.errors)

@server.route('/download')
def download():
    # Display results from the pdProcess function to the page
    output = pdDownload(pdGroupObject)
    return send_file(output, attachment_filename='testing.xlsx', as_attachment=True)

def run_server():
    # server.run(host="127.0.0.1", port=5100, threaded=True)
    server.run(debug=True)

if __name__ == "__main__":
    run_server()
