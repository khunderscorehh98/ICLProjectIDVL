from flask import Flask, render_template, request
from tasks.days_left import calculate_days

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/days_left', methods=['GET', 'POST'])
def days_left():
    result = {}
    if request.method == 'POST':
        graduation_date = request.form['graduation_date']
        result['total_days'], result['total_days_excl_final'], result['working_days'] = calculate_days(graduation_date)
    return render_template('days_left.html', result=result)
