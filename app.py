from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
      'id': 1,
      'title': 'Data Analyst',
      'location': 'Victoria, BC',
      'salary': '70K-90K'  
    },
    {
      'id': 2,
      'title': 'Frontend Developer',
      'location': 'Calgary, AB',
      'salary': '50K-60K'  
    },
    {
      'id': 3,
      'title': 'Backend Developer',
      'location': 'Vancouver, BC',
      'salary': '80K-110K'  
    },
    {
      'id': 4,
      'title': 'Security Analyst',
      'location': 'Kelowna, BC',
      'salary': ''  
    }
]

@app.route("/")
def index():
    return render_template("index.html", jobs=JOBS, company_name="Careers Website")
