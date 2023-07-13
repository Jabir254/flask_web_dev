from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location':'Nairobi',
        'salary': 'Kes. 400000'
    },
    {
        'id': 2,
        'title': 'Backend Engineer',
        'location':'Nairobi',
        'salary': 'Kes. 350000'
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'location':'Nairobi',
        'salary': 'Kes. 300000'
    },
    {
        'id': 4,
        'title': 'Data Analyst',
        'location':'Nairobi',
        'salary': 'Kes. 250000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True,
            host='0.0.0.0',
            port=8000)