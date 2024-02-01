from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
db = SQLAlchemy(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(255), nullable=False)
    deadline = db.Column(db.Integer, nullable=False)
    profit = db.Column(db.Integer, nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

@app.route('/sorted')
def sorted():
    return render_template('sorted.html')



@app.route('/add_job', methods=['POST'])
def add_job():
    try:
        job_name = request.form['job_name']
        deadline = int(request.form['deadline'])
        profit = int(request.form['profit'])

        if not job_name or deadline <= 0 or profit < 0:
            raise ValueError("Invalid form data")

        new_job = Job(job_name=job_name, deadline=deadline, profit=profit)
        db.session.add(new_job)
        db.session.commit()

        return redirect(url_for('index'))

    except ValueError as e:
        return render_template('error.html', error=str(e))

    except Exception as e:
        return render_template('error.html', error="An error occurred")
    
@app.route('/delete_job', methods=['POST'])
def delete_job():
    try:
        job_id = int(request.form['delete_index'])

        job_to_delete = Job.query.get(job_id)

        if job_to_delete:
            db.session.dele

    except Exception as e:
        return render_template('error.html', error="An error occurred")
    