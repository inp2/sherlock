#!/usr/bin/python

import datetime
import os

# Forensic Libraries
import pytsk3

# Flask Libraries
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
UPLOAD_FOLDER = 'cases/'

server = Flask(__name__)
server.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def getImageInfo(file_path):
    img = pytsk3.Img_Info(file_path)
    volume = pytsk3.Volume_Info(img)
    return volume
    
@server.route("/parser/<filename>")
# Parse Forensic Image
def image_parser(filename):
    file_path = "/home/groot/sherlock/app/cases/" + filename
    img = getImageInfo(file_path)
    return render_template("parser.html", img=str(img))

@server.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(server.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for("image_parser", filename=filename))
    return '''
    <!doctype html>
    <title>sherlock</title>
    <h1>sherlock: A Digital Forensic Analysis Toolkit</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''



if __name__ == '__main__':
    server.run(host='0.0.0.0', debug=True)
