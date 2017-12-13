from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask import render_template

import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST','localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '5redwood')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'donorsUSA')

app.config['MYSQL_DB_TABLE'] = os.getenv('MYSQL_DB_TABLE', 'projects')

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/graphs')
def graphs():
    return render_template("graphs.html")


@app.route("/donorsUSprojects")
def table_details():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT _projectid, funding_status, school_state, resource_type, poverty_level, date_posted, total_donations from {}'.format(os.getenv('MYSQL_DB_TABLE')))
    items = cursor.fetchall()
    results = []
    for _projectid, funding_status, school_state, resource_type, poverty_level, date_posted, total_donations in items:
        results.append({
            '_projectid': _projectid,
            'funding_status': funding_status,
            'school_state': school_state,
            'resource_type': resource_type,
            'poverty_level': poverty_level,
            'date_posted': date_posted,
            'total_donations': total_donations
        })
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)