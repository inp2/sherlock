from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory, make_response
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import networkx as nx
from causal import observe_evidence
from causal import formulate_evidence
from causal import evaluate_evidence
import os
import StringIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Create a global graph
digraph = nx.DiGraph()
# Create a global paths list
paths = []

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
def requester():
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
@app.route('/<filename>')
def uploaded_file(filename):
    h, pr, katz, dcent, dg = observe_evidence(filename)
    global digraph
    digraph = nx.DiGraph(dg)
    return render_template('observe.html', filename=filename, hubs=h, pagerank=pr, katz=katz, dcentrality=dcent)

@app.route('/formulate', methods=['POST'])
def formulate():    
    src = request.form['Source']
    trg = request.form['Target']
    # Modify global copy of graph
    global digraph
    # Modify global copy of paths
    global paths
    paths = formulate_evidence(src, trg, digraph)
    return render_template('formulate.html', paths=paths)

@app.route('/evaluate/<path>', methods=['POST'])
def evaluate(path):
    print "Hello"
    print "_____"
    global digraph
    global paths
    print path
    deg_dis = evaluate_evidence(digraph, paths)
    return render_template('evaluate.html', degdis=deg_dis)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
