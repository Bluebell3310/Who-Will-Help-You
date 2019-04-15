from why import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/project/<int:project_id>')
def project(project_id):
    return render_template('project.html')
