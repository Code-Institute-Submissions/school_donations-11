from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask import render_template

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5redwood'
app.config['MYSQL_DB'] = 'donorsUSA'

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
    cursor.execute('SELECT _projectid, funding_status, school_state, resource_type, poverty_level, date_posted, total_donations from projects')
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