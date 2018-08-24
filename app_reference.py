import sys
import threading
import webview
from flask import Flask, render_template, flash, redirect, url_for, request
from dataProcess import pdProcess
from wtforms import StringField, TextAreaField, PasswordField, validators
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

# Uploads config
UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

class UploadForm(FlaskForm):
    upload = FileField('Select a File', validators=[
        FileRequired(),
        FileAllowed(['csv', 'xls', 'xlsx'], 'Excel file formats only')
    ])

@app.route('/process', methods=['GET', 'POST'])
def process():
    form = UploadForm()
    if request.method == 'POST' and form.validate_on_submit():
        inputfile = form.upload.data

        # Display resuls from the pdProcess function to the page
        pdProcess(inputfile)

        flash('Spreadsheet successfully processed!', 'success')

        return redirect(url_for('process'))

    return render_template('process.html', form=form)

def start_server():
    app.secret_key = 'secretkey123'
    app.run()

if __name__ == '__main__':
    """  https://github.com/r0x0r/pywebview/blob/master/examples/http_server.py
    """
    # app.secret_key = 'secretkey123'
    # app.run(debug=True)
 
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
 
    webview.create_window("Data Ops", "http://127.0.0.1:5000/")
 
    sys.exit()