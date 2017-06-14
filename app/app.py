from flask import Flask, render_template, request, redirect, url_for, send_from_directory, make_response
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import networkx as nx
from causal import observe_evidence
import os
import StringIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Store the uploaded files
UPLOAD_FOLDER = 'uploads/'
# Set of allowed file extensions
ALLOWED_EXTENSIONS = set(['txt', 'csv', 'xml'])

# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# For a give file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# This route will show a form to start the case
@app.route('/')
def start_case():
    return render_template('form.html')

# Route that will process the file upload
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submist an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')
   
# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    dg = observe_evidence(filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
