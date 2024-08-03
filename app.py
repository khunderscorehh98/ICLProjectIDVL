from flask import Flask, render_template, request
from tasks.days_left import calculate_days
from tasks.brunei_ic import generate_brunei_ic, hide_password
from tasks.apartment_problem import calculate_max_profit
from tasks.search_backwards import last_greater_backwd

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

@app.route('/brunei_ic', methods=['GET', 'POST'])
def brunei_ic():
    result = {}
    if request.method == 'POST':
        name = request.form['name']
        nationality = request.form['nationality']
        user_id = request.form['user_id']
        password = request.form['password']
        result['name'] = name
        result['nationality'] = nationality
        result['user_id'] = user_id
        result['hidden_password'] = hide_password(password)
        result['brunei_ic'] = generate_brunei_ic(nationality)
    return render_template('brunei_ic.html', result=result)

@app.route('/apartment_problem', methods=['GET', 'POST'])
def apartment_problem():
    result = {}
    if request.method == 'POST':
        total_units = int(request.form['total_units'])
        rent = int(request.form['rent'])
        increase = int(request.form['increase'])
        maintenance = int(request.form['maintenance'])
        result['optimal_units'], result['max_profit'] = calculate_max_profit(total_units, rent, increase, maintenance)
    return render_template('apartment_problem.html', result=result)

@app.route('/search_backwards', methods=['GET', 'POST'])
def search_backwards():
    result = {}
    if request.method == 'POST':
        lst = list(map(int, request.form['list'].split(',')))
        num = int(request.form['num'])
        result['index'] = last_greater_backwd(lst, num)
    return render_template('search_backwards.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)