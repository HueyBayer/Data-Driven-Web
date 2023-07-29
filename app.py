from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Manila, Philippines',
    'salary': 'Php. 40,000'
  },
    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Cavite, Philippines'
  },
    {
    'id': 3,
    'title': 'Data Manager',
    'location': 'Laguna, Philippines',
    'salary': 'Php. 90,000'
  }
]

@app.route("/")
def hello_Jovian():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)
