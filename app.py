from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
      {
          'id': 1,
          'title': 'Data Analyst',
          'location': 'San Francisco',
          'salary': '$2478234'
      },
      {
          'id': 2,
          'title': 'Software Engineer',
          'location': 'New York',
          'salary': '$180000'
      },
      {
          'id': 3,
          'title': 'Product Manager',
          'location': 'Seattle',
          'salary': '$150000'
      },
      {
          'id': 4,
          'title': 'UX Designer',
          'location': 'Los Angeles',
          'salary': '$120000'
      },
      {
          'id': 5,
          'title': 'Data Scientist',
          'location': 'Chicago',
          'salary': '$160000'
      }
  ]


@app.route("/")
def hello_world():
      return render_template("home.html", jobs=JOBS, company_name="Jovian")


@app.route("/api/jobs")
def list_jobs():
      return jsonify(JOBS)


if __name__ == "__main__":
      app.run(host='0.0.0.0', debug=True)
