from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location':'Nairobi, Kenya',
        'salary': 'Kes. 400,000'
    },
    {
        'id': 2,
        'title': 'Backend Engineer',
        'location':'Nairobi, Kenya',
        'salary': 'Kes. 350,000'
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'location':'Nairobi, Kenya',
        'salary': 'Kes. 300,000'
    },
    {
        'id': 4,
        'title': 'Data Analyst',
        'location':'Nairobi, Kenya',
        'salary': 'Kes. 250,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs = JOBS)

@app.route('/jobs')
def list():
    return jsonify(JOBS)



if __name__ == "__main__":
    app.run(debug=True,
            host='0.0.0.0',
            port=8000)
