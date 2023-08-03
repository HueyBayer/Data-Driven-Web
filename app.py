from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
from sqlalchemy import text

app = Flask(__name__)

@app.route("/")
def hello_Jovian():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs_list = jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/apply/<id>")
def show_job(id):
  job_lists = load_job_from_db(id)
  if not job_lists:
    return "Not Found", 404
  return render_template("apply.html", job=job_lists)
  

@app.route("/apply/<id>/application", methods=['post'])
def apply_to_job(id):
  data = request.form
  job_lists = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template("submit.html", application=data, job=job_lists)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)
