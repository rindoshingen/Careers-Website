from flask import Flask, render_template
from data import JOBS

app = Flask(__name__)

company_name = 'Careers Website'
company_tagline = 'A Python Flask Test Career Website'

@app.context_processor
def inject_globals():
    return dict(company_name=company_name, company_tagline=company_tagline)

@app.route('/')
def index():
    return render_template(
        'index.html', 
        page_title='Homepage',
        show_header=True)

@app.route('/jobs')
def jobs():
    return render_template(
        'jobs.html', 
        jobs=JOBS,
        page_title='Jobs Page',
        show_header=True)

@app.route('/about')
def about():
    return render_template(
        'about.html',
        page_title='About Page',
        show_header=True)

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        page_title='Contact Page',
        show_header=True)